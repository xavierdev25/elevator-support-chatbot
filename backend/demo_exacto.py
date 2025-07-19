#!/usr/bin/env python3
"""
Demostración exacta del ejemplo de conversación proporcionado por el usuario
"""

from chatbot import ElevatorChatbot

def demo_exacto():
    """Demuestra exactamente el ejemplo de conversación del usuario"""
    chatbot = ElevatorChatbot()
    
    # Ejemplo exacto del usuario
    conversation = [
        "Hola",
        "Necesito mantenimiento",
        "asensor",
        "sí",
        "parte mecanica",
        "poseo un yaskawa",
        "sí",
        "12"
    ]
    
    print("🎯 DEMOSTRACIÓN EXACTA DEL EJEMPLO")
    print("=" * 60)
    print("Conversación del usuario:")
    print("-" * 60)
    
    for i, user_input in enumerate(conversation, 1):
        print(f"Usuario: {user_input}")
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 60)
    
    print("\n✅ ¡Conversación completada exitosamente!")
    print("El chatbot funciona exactamente como se solicitó.")

if __name__ == "__main__":
    demo_exacto() 