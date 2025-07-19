#!/bin/bash

# Script para iniciar el servidor del chatbot
echo "🎯 Chatbot de Mantenimiento de Ascensores"
echo "=========================================="

# Verificar si estamos en el directorio correcto
if [ ! -f "app.py" ]; then
    echo "❌ Error: No se encontró app.py en el directorio actual"
    echo "   Asegúrate de ejecutar este script desde el directorio backend/"
    exit 1
fi

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    echo "🔧 Activando entorno virtual..."
    source venv/bin/activate
else
    echo "⚠️  No se encontró entorno virtual. Creando uno nuevo..."
    python -m venv venv
    source venv/bin/activate
    echo "📦 Instalando dependencias..."
    pip install -r requirements.txt
fi

echo "🚀 Iniciando servidor..."
echo "📡 Servidor disponible en: http://localhost:5000"
echo "🔗 Frontend: Abre chat.html en tu navegador"
echo "🛑 Presiona Ctrl+C para detener el servidor"
echo ""

# Ejecutar el servidor
python app.py 