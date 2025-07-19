#!/usr/bin/env python3
"""
Servidor Flask para el Chatbot de Mantenimiento de Ascensores
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import ElevatorChatbot
import json

app = Flask(__name__)

# Configuración mejorada de CORS
CORS(app, 
     origins=["*"],  # Permitir todos los orígenes durante desarrollo
     supports_credentials=False,  # Cambiar a False ya que no necesitamos credenciales
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"])

# Instancia global del chatbot
chatbot = ElevatorChatbot()

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    """
    Endpoint para procesar mensajes del chatbot
    """
    # Manejar solicitudes OPTIONS (preflight)
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', request.headers.get('Origin', '*'))
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
    
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Mensaje requerido'}), 400
        
        user_message = data['message']
        mantenimiento_flujo = data.get('mantenimiento_flujo', None)
        
        # Si hay un flujo de mantenimiento guardado, restaurarlo
        if mantenimiento_flujo:
            chatbot.conversation_state = mantenimiento_flujo
        
        # Procesar el mensaje
        response = chatbot.get_response(user_message)
        
        # Devolver respuesta con el estado actual del flujo
        return jsonify({
            'response': response,
            'mantenimiento_flujo': chatbot.conversation_state
        })
        
    except Exception as e:
        print(f"Error en el endpoint /chat: {str(e)}")
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificar que el servidor está funcionando
    """
    return jsonify({'status': 'ok', 'message': 'Chatbot funcionando correctamente'})

@app.route('/reset', methods=['POST'])
def reset_conversation():
    """
    Endpoint para reiniciar la conversación
    """
    try:
        chatbot.reset_conversation()
        return jsonify({'message': 'Conversación reiniciada'})
    except Exception as e:
        return jsonify({'error': 'Error al reiniciar conversación'}), 500

@app.route('/catalogo', methods=['GET'])
def get_catalog():
    """
    Endpoint para obtener el catálogo de repuestos
    """
    try:
        # Importar la información del negocio
        from business_info import BUSINESS_INFO
        
        catalog = BUSINESS_INFO.get('spare_parts_catalog', {})
        return jsonify(catalog)
        
    except Exception as e:
        print(f"Error al obtener catálogo: {str(e)}")
        return jsonify({'error': 'Error al obtener catálogo'}), 500

if __name__ == '__main__':
    print("🚀 Iniciando servidor del Chatbot de Ascensores...")
    print("📡 Servidor disponible en: http://localhost:5000")
    print("🔗 Endpoints disponibles:")
    print("   - POST /chat - Procesar mensajes")
    print("   - GET  /health - Verificar estado")
    print("   - POST /reset - Reiniciar conversación")
    print("   - GET  /catalogo - Obtener catálogo")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True) 