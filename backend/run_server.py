#!/usr/bin/env python3
"""
Script para ejecutar el servidor del chatbot
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala las dependencias requeridas"""
    print("📦 Instalando dependencias...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        return False

def run_server():
    """Ejecuta el servidor Flask"""
    print("🚀 Iniciando servidor del chatbot...")
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
    except Exception as e:
        print(f"❌ Error al ejecutar el servidor: {e}")

def main():
    print("🎯 Chatbot de Mantenimiento de Ascensores")
    print("=" * 50)
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("app.py"):
        print("❌ Error: No se encontró app.py en el directorio actual")
        print("   Asegúrate de ejecutar este script desde el directorio backend/")
        return
    
    # Instalar dependencias
    if not install_requirements():
        return
    
    # Ejecutar servidor
    run_server()

if __name__ == "__main__":
    main() 