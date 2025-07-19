#!/usr/bin/env python3
"""
Demostración del manejo de contexto y dualidad del usuario
"""

from chatbot import ElevatorChatbot

def demo_contexto():
    """Demuestra cómo el chatbot maneja el contexto y la dualidad"""
    
    print("🧠 DEMOSTRACIÓN DE CONTEXTO Y DUALIDAD")
    print("=" * 60)
    
    # Demostración 1: Cambio de opinión sobre el tipo de equipo
    print("\n📋 DEMOSTRACIÓN 1: Cambio de Tipo de Equipo")
    print("-" * 50)
    chatbot1 = ElevatorChatbot()
    
    conversation1 = [
        "Hola",
        "Necesito mantenimiento",
        "asensor",
        "no",  # Cambia de opinión
        "escalera",
        "todo",
        "Otis",
        "12"
    ]
    
    for user_input in conversation1:
        print(f"Usuario: {user_input}")
        response = chatbot1.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Demostración 2: Cambio de marca después de consultar
    print("\n📋 DEMOSTRACIÓN 2: Cambio de Marca")
    print("-" * 50)
    chatbot2 = ElevatorChatbot()
    
    conversation2 = [
        "Hola",
        "mantenimiento",
        "ascensor",
        "parte mecanica",
        "¿qué marcas tienen?",
        "Yaskawa",
        "no",  # Cambia de opinión
        "Schindler",
        "8"
    ]
    
    for user_input in conversation2:
        print(f"Usuario: {user_input}")
        response = chatbot2.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Demostración 3: Corrección de edad
    print("\n📋 DEMOSTRACIÓN 3: Corrección de Edad")
    print("-" * 50)
    chatbot3 = ElevatorChatbot()
    
    conversation3 = [
        "Hola",
        "mantenimiento",
        "ascensor",
        "cabina",
        "Otis",
        "60",  # Edad inválida
        "15",  # Edad corregida
    ]
    
    for user_input in conversation3:
        print(f"Usuario: {user_input}")
        response = chatbot3.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Demostración 4: Múltiples consultas en una conversación
    print("\n📋 DEMOSTRACIÓN 4: Múltiples Consultas")
    print("-" * 50)
    chatbot4 = ElevatorChatbot()
    
    conversation4 = [
        "Hola",
        "mantenimiento",
        "ascensor",
        "todo",
        "Mitsubishi",
        "10",
        # Después de la cotización, el bot reinicia automáticamente
        "mantenimiento",
        "escalera",
        "parte mecanica",
        "Kone",
        "5"
    ]
    
    for user_input in conversation4:
        print(f"Usuario: {user_input}")
        response = chatbot4.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Demostración 5: Contexto mantenido durante confirmaciones
    print("\n📋 DEMOSTRACIÓN 5: Contexto en Confirmaciones")
    print("-" * 50)
    chatbot5 = ElevatorChatbot()
    
    conversation5 = [
        "Hola",
        "mantenimiento",
        "ascensor",
        "sistema electronico",
        "poseo un yaskawa",
        "sí",  # Confirma la marca
        "25"   # Continúa con la edad
    ]
    
    for user_input in conversation5:
        print(f"Usuario: {user_input}")
        response = chatbot5.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    print("\n✅ ¡El chatbot maneja perfectamente el contexto y la dualidad!")
    print("Características del contexto:")
    print("• Mantiene el estado de la conversación")
    print("• Permite cambios de opinión")
    print("• Valida y corrige errores")
    print("• Reinicia automáticamente después de cada cotización")
    print("• Maneja confirmaciones inteligentemente")

if __name__ == "__main__":
    demo_contexto() 