#!/usr/bin/env python3
"""
Demostración completa de todas las funcionalidades del chatbot
"""

from chatbot import ElevatorChatbot

def demo_completo():
    """Demuestra todas las funcionalidades implementadas"""
    
    print("🤖 DEMOSTRACIÓN COMPLETA DEL CHATBOT")
    print("=" * 80)
    
    print("\n🎯 **FUNCIONALIDADES IMPLEMENTADAS:**\n")
    print("1. 🚨 **Emergencias** - Respuesta inmediata con pasos claros")
    print("2. 💰 **Precios por marca** - Cotizaciones con redirección")
    print("3. 🏢 **Recomendaciones** - Ascensores por tipo de edificio")
    print("4. 🎯 **Casos especiales** - Discapacidad, colegios, etc.")
    print("5. 📅 **Agendamiento** - Citas y contactos")
    print("6. ❓ **Preguntas frecuentes** - Información general")
    print("7. 🔧 **Repuestos** - Catálogo completo con precios")
    print("8. 🛠️ **Mantenimiento** - Flujo completo de cotización")
    print("9. 🏗️ **Modernización** - Información detallada")
    print("10. 🙏 **Atención al cliente** - Agradecimientos y cierre")
    
    print("\n" + "=" * 80)
    print("💬 **EJEMPLOS DE CONVERSACIÓN:**\n")
    
    # Ejemplo 1: Emergencia
    print("🚨 **EJEMPLO 1: EMERGENCIA**")
    print("-" * 40)
    chatbot1 = ElevatorChatbot()
    print("Usuario: Estoy atrapada en un ascensor, necesito ayuda urgente")
    response = chatbot1.get_response("Estoy atrapada en un ascensor, necesito ayuda urgente")
    print(f"Bot: {response[:300]}...")
    print()
    
    # Ejemplo 2: Precio por marca
    print("💰 **EJEMPLO 2: PRECIO POR MARCA**")
    print("-" * 40)
    chatbot2 = ElevatorChatbot()
    print("Usuario: ¿Cuánto cuesta un ascensor de la marca Schindler?")
    response = chatbot2.get_response("¿Cuánto cuesta un ascensor de la marca Schindler?")
    print(f"Bot: {response[:300]}...")
    print()
    
    # Ejemplo 3: Recomendación
    print("🏢 **EJEMPLO 3: RECOMENDACIÓN**")
    print("-" * 40)
    chatbot3 = ElevatorChatbot()
    print("Usuario: Para un edificio que ascensor me recomiendas")
    response = chatbot3.get_response("Para un edificio que ascensor me recomiendas")
    print(f"Bot: {response[:300]}...")
    print()
    
    # Ejemplo 4: Caso especial
    print("♿ **EJEMPLO 4: CASO ESPECIAL**")
    print("-" * 40)
    chatbot4 = ElevatorChatbot()
    print("Usuario: En casa que se puede instalar para una persona discapacitada")
    response = chatbot4.get_response("En casa que se puede instalar para una persona discapacitada")
    print(f"Bot: {response[:300]}...")
    print()
    
    # Ejemplo 5: Repuestos
    print("🔧 **EJEMPLO 5: REPUESTOS**")
    print("-" * 40)
    chatbot5 = ElevatorChatbot()
    print("Usuario: Necesito un variador VF5")
    response = chatbot5.get_response("Necesito un variador VF5")
    print(f"Bot: {response[:300]}...")
    print()
    
    # Ejemplo 6: Mantenimiento completo
    print("🛠️ **EJEMPLO 6: MANTENIMIENTO COMPLETO**")
    print("-" * 40)
    chatbot6 = ElevatorChatbot()
    conversation = [
        "Hola, necesito mantenimiento",
        "Ascensor",
        "Sistema electrónico",
        "Otis",
        "15"
    ]
    
    for i, user_input in enumerate(conversation, 1):
        print(f"Usuario: {user_input}")
        response = chatbot6.get_response(user_input)
        if i == len(conversation):
            print(f"Bot: {response[:300]}...")
        else:
            print(f"Bot: {response}")
        print()
    
    # Ejemplo 7: Modernización
    print("🏗️ **EJEMPLO 7: MODERNIZACIÓN**")
    print("-" * 40)
    chatbot7 = ElevatorChatbot()
    conversation = [
        "Quiero modernizar mi escalera eléctrica",
        "Completa"
    ]
    
    for i, user_input in enumerate(conversation, 1):
        print(f"Usuario: {user_input}")
        response = chatbot7.get_response(user_input)
        if i == len(conversation):
            print(f"Bot: {response[:300]}...")
        else:
            print(f"Bot: {response}")
        print()
    
    # Ejemplo 8: Preguntas frecuentes
    print("❓ **EJEMPLO 8: PREGUNTAS FRECUENTES**")
    print("-" * 40)
    chatbot8 = ElevatorChatbot()
    print("Usuario: ¿Qué servicios ofrecen?")
    response = chatbot8.get_response("¿Qué servicios ofrecen?")
    print(f"Bot: {response[:300]}...")
    print()
    
    # Ejemplo 9: Agendamiento
    print("📅 **EJEMPLO 9: AGENDAMIENTO**")
    print("-" * 40)
    chatbot9 = ElevatorChatbot()
    print("Usuario: Quiero agendar un mantenimiento preventivo")
    response = chatbot9.get_response("Quiero agendar un mantenimiento preventivo")
    print(f"Bot: {response[:300]}...")
    print()
    
    # Ejemplo 10: Agradecimiento
    print("🙏 **EJEMPLO 10: AGRADECIMIENTO**")
    print("-" * 40)
    chatbot10 = ElevatorChatbot()
    print("Usuario: Muchas gracias por la información")
    response = chatbot10.get_response("Muchas gracias por la información")
    print(f"Bot: {response}")
    print()
    
    print("=" * 80)
    print("✅ **RESUMEN DE FUNCIONALIDADES:**\n")
    print("🎯 **PRIORIDADES IMPLEMENTADAS:**")
    print("• 🚨 Emergencias (máxima prioridad)")
    print("• 💰 Cotizaciones con redirección")
    print("• 🏢 Recomendaciones específicas")
    print("• 🎯 Casos especiales")
    print("• 📅 Agendamiento de servicios")
    print("• ❓ Preguntas frecuentes")
    print("• 🔧 Catálogo de repuestos")
    print("• 🛠️ Flujo de mantenimiento")
    print("• 🏗️ Información de modernización")
    print("• 🙏 Atención al cliente")
    
    print("\n📞 **REDIRECCIÓN A CONTACTOS:**")
    print("• WhatsApp: +51 xxxxxxxxx")
    print("• Teléfono: +51 xxxxxxxxx")
    print("• Email: xxxxxxxxxxxxxxx")
    
    print("\n🎉 **¡CHATBOT COMPLETAMENTE FUNCIONAL!**")

if __name__ == "__main__":
    demo_completo() 