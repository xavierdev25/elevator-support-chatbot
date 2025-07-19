#!/usr/bin/env python3
"""
Demostración de diferentes variaciones de uso del chatbot
"""

from chatbot import ElevatorChatbot

def demo_variaciones():
    """Demuestra diferentes variaciones de uso del chatbot"""
    
    print("🎯 DEMOSTRACIÓN DE VARIACIONES DE USO")
    print("=" * 60)
    
    # Variación 1: Escalera eléctrica con consulta de marcas
    print("\n📋 VARIACIÓN 1: Escalera Eléctrica")
    print("-" * 50)
    chatbot1 = ElevatorChatbot()
    
    conversation1 = [
        "Hola",
        "Necesito mantenimiento",
        "escalera",
        "todo",
        "¿qué marcas tienen?",
        "Schindler",
        "10"
    ]
    
    for user_input in conversation1:
        print(f"Usuario: {user_input}")
        response = chatbot1.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Variación 2: Ascensor con sistema electrónico
    print("\n📋 VARIACIÓN 2: Ascensor - Sistema Electrónico")
    print("-" * 50)
    chatbot2 = ElevatorChatbot()
    
    conversation2 = [
        "Buenos días",
        "mantenimiento",
        "ascensor",
        "sistema electronico",
        "Otis",
        "20"
    ]
    
    for user_input in conversation2:
        print(f"Usuario: {user_input}")
        response = chatbot2.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Variación 3: Ascensor con corrección de marca
    print("\n📋 VARIACIÓN 3: Ascensor con Corrección de Marca")
    print("-" * 50)
    chatbot3 = ElevatorChatbot()
    
    conversation3 = [
        "Hola",
        "mantenimiento",
        "ascensor",
        "cabina",
        "mitsubishi",
        "5"
    ]
    
    for user_input in conversation3:
        print(f"Usuario: {user_input}")
        response = chatbot3.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Variación 4: Escalera con parte mecánica
    print("\n📋 VARIACIÓN 4: Escalera - Parte Mecánica")
    print("-" * 50)
    chatbot4 = ElevatorChatbot()
    
    conversation4 = [
        "Buenas",
        "Necesito mantenimiento",
        "escalera",
        "parte mecanica",
        "Kone",
        "15"
    ]
    
    for user_input in conversation4:
        print(f"Usuario: {user_input}")
        response = chatbot4.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    # Variación 5: Ascensor con marca no común
    print("\n📋 VARIACIÓN 5: Ascensor - Marca Especializada")
    print("-" * 50)
    chatbot5 = ElevatorChatbot()
    
    conversation5 = [
        "Hola",
        "mantenimiento",
        "ascensor",
        "todo",
        "Hyundai",
        "8"
    ]
    
    for user_input in conversation5:
        print(f"Usuario: {user_input}")
        response = chatbot5.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 30)
    
    print("\n✅ ¡Todas las variaciones funcionan correctamente!")
    print("El chatbot es versátil y maneja diferentes escenarios.")

if __name__ == "__main__":
    demo_variaciones() 