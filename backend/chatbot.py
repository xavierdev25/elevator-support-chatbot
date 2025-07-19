import re
from typing import Dict, List, Optional, Tuple
from business_info import BUSINESS_INFO

class ElevatorChatbot:
    def __init__(self):
        self.conversation_state = {
            "equipment_type": None,  # "ascensor" o "escalera"
            "brand": None,
            "sector": None,
            "age": None,
            "confirmed_brand": False,
            "confirmed_equipment": False,
            "waiting_for_confirmation": False,
            "service_type": None,  # "mantenimiento" o "modernizacion"
            "modernization_scope": None  # "basica" o "completa"
        }
        self.reset_conversation()
    
    def reset_conversation(self):
        """Reinicia el estado de la conversación"""
        self.conversation_state = {
            "equipment_type": None,
            "brand": None,
            "sector": None,
            "age": None,
            "confirmed_brand": False,
            "confirmed_equipment": False,
            "waiting_for_confirmation": False,
            "service_type": None,
            "modernization_scope": None
        }
    
    def normalize_text(self, text: str) -> str:
        """Normaliza el texto para comparaciones"""
        return text.lower().strip()
    
    def find_best_match(self, user_input: str, options: List[str]) -> Optional[str]:
        """Encuentra la mejor coincidencia entre la entrada del usuario y las opciones disponibles"""
        normalized_input = self.normalize_text(user_input)
        
        # Coincidencias exactas
        for option in options:
            if self.normalize_text(option) == normalized_input:
                return option
        
        # Coincidencias parciales
        for option in options:
            normalized_option = self.normalize_text(option)
            if normalized_option in normalized_input or normalized_input in normalized_option:
                return option
        
        # Coincidencias por similitud (para casos como "asensor" -> "Ascensor")
        common_mistakes = {
            "asensor": "Ascensor",
            "ascensor": "Ascensor",
            "elevador": "Ascensor",
            "escalera": "Escalera eléctrica",
            "escalera electrica": "Escalera eléctrica",
            "parte mecanica": "parte mecánica",
            "parte mecanica": "parte mecánica",
            "sistema electronico": "sistema electrónico",
            "sistema electronico": "sistema electrónico",
            "yaskawa": "Yaskawa",
            "otis": "Otis",
            "schindler": "Schindler",
            "kone": "Kone",
            "orona": "Orona",
            "mitsubishi": "Mitsubishi",
            "thyssenkrupp": "Thyssenkrupp",
            "hyundai": "Hyundai",
            "omega": "Omega",
            "fujiyida": "Fujiyida",
            "wilcox": "Wilcox",
            "kuesta": "cuesta",
            "kosto": "costo",
            "ke": "que",
            "k": "que",
            "komponente": "componente",
            "kontakto": "contacto",
            "kontrato": "contrato",
            "kotizacion": "cotización",
            "diagnostiko": "diagnóstico",
            "kita": "cita",
            "tecniko": "técnico",
            "grasias": "gracias",
            "ola": "hola",
            "kede": "quedé",
            "k tal": "qué tal",
            "buenos dias": "buenos días",
            "buen dia": "buen día",
            "electroniko": "electrónico",
            "electronica": "electrónica",
            "modernizacion": "modernización",
            "renovacion": "renovación",
            "atencion": "atención",
            "informacion": "información",
            "revision": "revisión",
            "servicio": "servicio",
            "mantenimiento": "mantenimiento",
            "emergencia": "emergencia",
            "ayuda": "ayuda",
            "problema": "problema",
            "ruido": "ruido",
            "lento": "lento",
            "puerta": "puerta",
            "boton": "botón",
            "funciona": "funciona",
            "no funciona": "no funciona"
        }
        
        # Buscar coincidencias con errores ortográficos
        for mistake, correction in common_mistakes.items():
            if mistake in normalized_input:
                # Reemplazar el error con la corrección
                corrected_input = normalized_input.replace(mistake, correction)
                # Buscar coincidencia con la entrada corregida
                for option in options:
                    if self.normalize_text(option) == corrected_input:
                        return option
                    normalized_option = self.normalize_text(option)
                    if corrected_input in normalized_option or normalized_option in corrected_input:
                        return option
        
        # Buscar coincidencias directas con errores comunes
        return common_mistakes.get(normalized_input)
    
    def validate_age(self, age_input: str) -> Optional[int]:
        """Valida que la edad sea un número entre 1 y 50"""
        try:
            age = int(age_input)
            if 1 <= age <= 50:
                return age
            return None
        except ValueError:
            return None
    
    def calculate_maintenance_price(self) -> int:
        """Calcula el precio del mantenimiento basado en los datos recopilados"""
        if not all([self.conversation_state["equipment_type"], 
                   self.conversation_state["brand"], 
                   self.conversation_state["sector"], 
                   self.conversation_state["age"]]):
            return 0
        
        equipment_type = self.conversation_state["equipment_type"]
        brand = self.conversation_state["brand"]
        sector = self.conversation_state["sector"]
        age = self.conversation_state["age"]
        
        pricing = BUSINESS_INFO["maintenance_pricing"][equipment_type]
        
        # Precio base por marca
        base_price = pricing["by_brand"].get(brand, pricing["base"])
        
        # Ajuste por sector
        sector_adjustment = pricing["sector_adjustment"].get(sector, 0)
        
        # Ajuste por edad
        age_adjustment = 0
        for age_range in pricing["age_adjustment"]:
            if age_range["min"] <= age <= age_range["max"]:
                age_adjustment = age_range["adjustment"]
                break
        
        total_price = base_price + sector_adjustment + age_adjustment
        return total_price
    
    def calculate_modernization_price(self) -> dict:
        """Calcula el precio de modernización basado en el tipo de equipo y alcance"""
        equipment_type = self.conversation_state["equipment_type"]
        scope = self.conversation_state["modernization_scope"]
        
        if not equipment_type or not scope:
            return None
        
        pricing = BUSINESS_INFO["modernization_pricing"][equipment_type]
        
        if scope == "basica":
            return {
                "usd_range": f"${pricing['basic']['usd_min']:,} - ${pricing['basic']['usd_max']:,} USD",
                "soles_range": f"S/. {pricing['basic']['soles_min']:,} - S/. {pricing['basic']['soles_max']:,} soles",
                "description": pricing['basic']['description']
            }
        elif scope == "completa":
            return {
                "usd_range": f"${pricing['complete']['usd_min']:,} - ${pricing['complete']['usd_max']:,} USD",
                "soles_range": f"S/. {pricing['complete']['soles_min']:,} - S/. {pricing['complete']['soles_max']:,} soles",
                "description": pricing['complete']['description']
            }
        
        return None
    
    def generate_modernization_info(self) -> str:
        """Genera información completa sobre modernización"""
        equipment_type = self.conversation_state["equipment_type"]
        equipment_display = "Ascensor" if equipment_type == "ascensor" else "Escalera eléctrica"
        
        pricing = BUSINESS_INFO["modernization_pricing"][equipment_type]
        
        info = (
            f"🏗️ **MODERNIZACIÓN DE {equipment_display.upper()}**\n\n"
            f"**Factores que influyen en el precio:**\n"
        )
        
        for factor in BUSINESS_INFO["modernization_factors"]:
            info += f"• {factor}\n"
        
        info += f"\n**Costos estimados:**\n"
        info += f"• **Modernización Básica:** ${pricing['basic']['usd_min']:,} - ${pricing['basic']['usd_max']:,} USD / S/. {pricing['basic']['soles_min']:,} - S/. {pricing['basic']['soles_max']:,} soles\n"
        info += f"• **Proyecto Completo:** ${pricing['complete']['usd_min']:,} - ${pricing['complete']['usd_max']:,} USD / S/. {pricing['complete']['soles_min']:,} - S/. {pricing['complete']['soles_max']:,} soles\n"
        info += f"• **Promedio en Lima:** S/. {pricing['average_soles']['min']:,} - S/. {pricing['average_soles']['max']:,} soles\n\n"
        
        info += f"**Beneficios de modernizar:**\n"
        for benefit in BUSINESS_INFO["modernization_benefits"]:
            info += f"• {benefit}\n"
        
        info += f"\n**¿Cómo obtener una cotización precisa?**\n"
        info += BUSINESS_INFO["modernization_quote_info"]
        
        info += f"\n\n📞 **Contacto:**\n"
        info += f"• Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
        info += f"• Email: {BUSINESS_INFO['contact_email']}\n"
        info += f"• Horario: {BUSINESS_INFO['hours']}"
        
        return info
    
    def handle_modernization_request(self, user_input: str) -> str:
        """Maneja las consultas específicas de modernización"""
        normalized_input = self.normalize_text(user_input)
        
        # Selección de tipo de equipo para modernización
        if not self.conversation_state["equipment_type"]:
            if "ascensor" in normalized_input or "asensor" in normalized_input or "elevador" in normalized_input:
                self.conversation_state["equipment_type"] = "ascensor"
                return "¿Qué tipo de modernización desea? (Básica o Completa)"
            elif "escalera" in normalized_input:
                self.conversation_state["equipment_type"] = "escalera"
                return "¿Qué tipo de modernización desea? (Básica o Completa)"
            else:
                return "Por favor, especifica si desea modernización para Ascensor o Escalera eléctrica."
        
        # Selección del alcance de modernización
        if not self.conversation_state["modernization_scope"]:
            if "basica" in normalized_input or "básica" in normalized_input or "basico" in normalized_input or "básico" in normalized_input:
                self.conversation_state["modernization_scope"] = "basica"
                return self.generate_modernization_info()
            elif "completa" in normalized_input or "completo" in normalized_input or "integral" in normalized_input:
                self.conversation_state["modernization_scope"] = "completa"
                return self.generate_modernization_info()
            else:
                return "Por favor selecciona el tipo de modernización: Básica (renovación de componentes esenciales) o Completa (proyecto integral con mejora estética)"
        
        # Si ya tenemos toda la información, mostrar la información
        return self.generate_modernization_info()
    
    def get_response(self, user_input: str) -> str:
        """Procesa la entrada del usuario y devuelve la respuesta apropiada"""
        normalized_input = self.normalize_text(user_input)
        
        # EMERGENCIAS - PRIORIDAD MÁXIMA
        if any(word in normalized_input for word in ["atrapada", "atrapado", "atrapada en", "atrapado en", "emergencia", "ayuda urgente", "asustada", "asustado", "kede", "quedé", "kede atrapada", "quedé atrapada", "ayuda ya", "ayuda inmediata", "socorro", "urgente"]):
            return self.handle_emergency(user_input)
        
        # Saludos iniciales
        if any(greeting in normalized_input for greeting in ["hola", "buenos dias", "buenas", "buen dia"]):
            return "¡Hola! 😊 ¿En qué puedo ayudarte hoy?\n\nPuedo asistirte con:\n• 🛠️ **Mantenimiento** de ascensores y escaleras eléctricas\n• 🏗️ **Modernización** de equipos\n• 🆘 **Emergencias** 24/7\n• 💰 **Cotizaciones** y precios\n• ❓ **Preguntas frecuentes**\n\n¿Qué servicio necesitas?"
        
        # PREGUNTAS FRECUENTES ESPECÍFICAS
        if "cuanto cuesta" in normalized_input and "ascensor" in normalized_input and "marca" in normalized_input:
            return self.handle_brand_price_query(user_input)
        
        if "que ascensor me recomiendas" in normalized_input or "que ascensor recomiendas" in normalized_input:
            return self.handle_recommendation_query(user_input)
        
        if "persona discapacitada" in normalized_input or "discapacidad" in normalized_input:
            return self.handle_disability_query()
        
        if "colegio" in normalized_input and ("cuanto" in normalized_input or "costo" in normalized_input):
            return self.handle_school_elevator_query()
        
        if "modernizacion" in normalized_input and "ascensor" in normalized_input and ("cuanto" in normalized_input or "costo" in normalized_input):
            return self.handle_elevator_modernization_query()
        
        if "contactar tecnico" in normalized_input or "tecnico" in normalized_input:
            return self.handle_technician_contact()
        
        if "agendar" in normalized_input or "cita" in normalized_input or "programar" in normalized_input:
            return self.handle_appointment_request()
        
        # NUEVAS CONSULTAS ESPECÍFICAS
        if "asistencia tecnica" in normalized_input or "asistencia técnica" in normalized_input or "soporte tecnico" in normalized_input or "soporte técnico" in normalized_input:
            return self.handle_technical_support_query()
        
        if ("precio" in normalized_input or "costo" in normalized_input or "cuanto" in normalized_input) and "escalera" in normalized_input:
            return self.handle_escalator_price_query()
        
        # CONSULTAS ESPECÍFICAS DE ESCALERAS ELÉCTRICAS - PRIORIDAD ALTA
        if ("modernizacion" in normalized_input or "modernización" in normalized_input) and "escalera" in normalized_input:
            return self.handle_escalator_modernization_query()
        
        if "mantenimiento" in normalized_input and "escalera" in normalized_input:
            # Establecer el tipo de servicio y equipo
            self.conversation_state["service_type"] = "mantenimiento"
            self.conversation_state["equipment_type"] = "escalera"
            return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
        
        if ("cotizacion" in normalized_input or "cotización" in normalized_input) and "escalera" in normalized_input:
            return self.handle_escalator_price_query()
        
        if "gracias" in normalized_input or "grasias" in normalized_input:
            return "¡De nada! 😊 Estoy aquí para ayudarte. Si tienes más preguntas o necesitas asistencia, no dudes en contactarme. ¡Que tengas un excelente día!"
        
        # PREGUNTAS FRECUENTES GENERALES
        if "que servicios" in normalized_input or "servicios ofrecen" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["servicios_generales"]["que_servicios"]
        
        if "mantenimiento escaleras" in normalized_input or "escaleras electricas" in normalized_input:
            return "Sí, ofrecemos mantenimiento completo para escaleras eléctricas de todas las marcas principales. Incluye revisión de componentes mecánicos, eléctricos y de seguridad."
        
        if "contrato mantenimiento" in normalized_input or "que incluye" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["servicios_generales"]["opciones_mantenimiento"]
        
        if "24 horas" in normalized_input or "emergencia" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["servicios_generales"]["servicio_emergencia"]
        
        if "mantenimiento preventivo" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["mantenimiento"]["mantenimiento_preventivo"]
        
        if "componentes revisan" in normalized_input or "que revisan" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["mantenimiento"]["componentes_revision"]
        
        if "todas marcas" in normalized_input or "trabajan marcas" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["mantenimiento"]["todas_marcas"]
        
        if "mantenimiento correctivo" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["mantenimiento"]["mantenimiento_correctivo"]
        
        if "repuestos" in normalized_input and ("venden" in normalized_input or "originales" in normalized_input):
            return BUSINESS_INFO["faq_responses"]["repuestos_modernizacion"]["venden_repuestos"]
        
        if "ventajas modernizar" in normalized_input or "beneficios modernizar" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["repuestos_modernizacion"]["ventajas_modernizar"]
        
        if "componentes renovar" in normalized_input or "que se puede renovar" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["repuestos_modernizacion"]["componentes_renovar"]
        
        if "ascensores ecologicos" in normalized_input or "gearless" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["ascensores_ecologicos"]["que_son"]
        
        if "por que eficientes" in normalized_input or "eficiencia" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["ascensores_ecologicos"]["por_que_eficientes"]
        
        if "diagnostico gratuito" in normalized_input or "evaluacion" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["diagnostico_proyectos"]["diagnostico_gratuito"]
        
        if "proyectos inconclusos" in normalized_input or "instalacion inconclusa" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["diagnostico_proyectos"]["proyectos_inconclusos"]
        
        if "cotizacion" in normalized_input or "cotizar" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["contacto_cotizaciones"]["solicitar_cotizacion"]
        
        if "horarios" in normalized_input or "atencion" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["contacto_cotizaciones"]["horarios_atencion"]
        
        if "ubicacion" in normalized_input or "donde" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["contacto_cotizaciones"]["ubicacion"]
        
        if "tipos ascensores" in normalized_input or "residenciales comerciales" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["detalles_tecnicos"]["tipos_ascensores"]
        
        if "plataformas discapacitados" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["detalles_tecnicos"]["plataformas_escaleras"]
        
        if "sistemas seguridad" in normalized_input or "seguridad" in normalized_input:
            return BUSINESS_INFO["faq_responses"]["detalles_tecnicos"]["sistemas_seguridad"]
        
        # CONSULTAS DE REPUESTOS ESPECÍFICOS
        if "repuesto" in normalized_input or "componente" in normalized_input or "variador" in normalized_input or "tarjeta" in normalized_input or "contacto" in normalized_input or "pulsador" in normalized_input:
            return self.handle_spare_parts_query(user_input)
        
        # Detección de tipo de servicio (mantenimiento o modernización) - PRIORIDAD ALTA
        if not self.conversation_state["service_type"]:
            if any(word in normalized_input for word in ["modernizacion", "modernización", "renovar", "renovacion", "renovación"]):
                self.conversation_state["service_type"] = "modernizacion"
                return "¿Sobre qué equipo desea la modernización? (Ascensor o Escalera eléctrica)"
            elif "mantenimiento" in normalized_input:
                self.conversation_state["service_type"] = "mantenimiento"
                return "¿Sobre qué equipo desea el mantenimiento? (Ascensor o Escalera eléctrica)"
        
        # Si es modernización, manejar de forma diferente
        if self.conversation_state["service_type"] == "modernizacion":
            return self.handle_modernization_request(user_input)
        
        # Si es mantenimiento, continuar con el flujo normal
        if self.conversation_state["service_type"] == "mantenimiento":
            # Procesamiento de información completa en una sola entrada (prioridad alta)
            if not self.conversation_state["equipment_type"]:
                # Buscar tipo de equipo en la entrada
                if "ascensor" in normalized_input or "asensor" in normalized_input or "elevador" in normalized_input:
                    self.conversation_state["equipment_type"] = "ascensor"
                elif "escalera" in normalized_input:
                    self.conversation_state["equipment_type"] = "escalera"
                
                # Si se encontró el tipo de equipo, buscar sector
                if self.conversation_state["equipment_type"]:
                    sector_options = ["cabina", "parte mecánica", "sistema electrónico", "todo"]
                    for sector in sector_options:
                        if sector in normalized_input:
                            self.conversation_state["sector"] = sector
                            break
                    
                    # Si se encontró el sector, buscar marca
                    if self.conversation_state["sector"]:
                        # Verificar si el usuario está preguntando por marcas
                        if any(word in normalized_input for word in ["marcas", "que marcas", "qué marcas", "marca", "brands"]):
                            equipment_type = self.conversation_state["equipment_type"]
                            if equipment_type == "ascensor":
                                brands = BUSINESS_INFO["elevator_brands"]
                            else:
                                brands = BUSINESS_INFO["escalator_brands"]
                            
                            brands_text = ", ".join(brands)
                            return f"Las marcas disponibles para {equipment_type} son: {brands_text}"
                        
                        equipment_type = self.conversation_state["equipment_type"]
                        if equipment_type == "ascensor":
                            available_brands = BUSINESS_INFO["elevator_brands"]
                        else:
                            available_brands = BUSINESS_INFO["escalator_brands"]
                        
                        for brand in available_brands:
                            if self.normalize_text(brand) in normalized_input:
                                self.conversation_state["brand"] = brand
                                break
                        
                        # Si se encontró la marca, buscar edad
                        if self.conversation_state["brand"]:
                            # Buscar números en el texto
                            import re
                            numbers = re.findall(r'\d+', user_input)
                            if numbers:
                                age = self.validate_age(numbers[0])
                                if age is not None:
                                    self.conversation_state["age"] = age
                                    return self.generate_price_quote()
                            
                            # Si no se encontró edad, preguntar por ella
                            return "¿Cuántos años de antigüedad tiene el equipo? (Por favor, ingrese un número entre 1 y 50)"
                        
                        # Si no se encontró marca, preguntar por ella
                        return "¿De qué marca es su equipo? (Puedes preguntar '¿qué marcas tienen?' para ver la lista)"
                    
                    # Si no se encontró sector, preguntar por él
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
            
            # Detección de cambios de contexto (prioridad alta)
            if self.conversation_state["equipment_type"]:
                # Cambio de ascensor a escalera
                if "escalera" in normalized_input and self.conversation_state["equipment_type"] == "ascensor":
                    self.reset_conversation()
                    self.conversation_state["equipment_type"] = "escalera"
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
                
                # Cambio de escalera a ascensor
                if ("ascensor" in normalized_input or "elevador" in normalized_input) and self.conversation_state["equipment_type"] == "escalera":
                    self.reset_conversation()
                    self.conversation_state["equipment_type"] = "ascensor"
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
            
            # Solicitud de mantenimiento
            if "mantenimiento" in normalized_input:
                return "¿Sobre qué equipo desea el mantenimiento? (Ascensor o Escalera eléctrica)"
            
            # Si estamos esperando confirmación de marca
            if self.conversation_state["waiting_for_confirmation"] and self.conversation_state["brand"]:
                if normalized_input in ["si", "sí", "yes"]:
                    self.conversation_state["confirmed_brand"] = True
                    self.conversation_state["waiting_for_confirmation"] = False
                    return "¿Cuántos años de antigüedad tiene el equipo? (Por favor, ingrese un número entre 1 y 50)"
                elif normalized_input in ["no"]:
                    self.conversation_state["brand"] = None
                    self.conversation_state["waiting_for_confirmation"] = False
                    return "¿De qué marca es su equipo? (Puedes preguntar '¿qué marcas tienen?' para ver la lista)"
                else:
                    return "Por favor responde sí o no."
            
            # Si estamos esperando confirmación de equipo
            if self.conversation_state["waiting_for_confirmation"] and self.conversation_state["equipment_type"] == "ascensor":
                if normalized_input in ["si", "sí", "yes"]:
                    self.conversation_state["confirmed_equipment"] = True
                    self.conversation_state["waiting_for_confirmation"] = False
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
                elif normalized_input in ["no"]:
                    self.conversation_state["equipment_type"] = "escalera"
                    self.conversation_state["confirmed_equipment"] = True
                    self.conversation_state["waiting_for_confirmation"] = False
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
                else:
                    return "Por favor responde sí o no."
            
            # Selección de tipo de equipo
            if not self.conversation_state["equipment_type"]:
                if "ascensor" in normalized_input or "asensor" in normalized_input or "elevador" in normalized_input:
                    self.conversation_state["equipment_type"] = "ascensor"
                    if "asensor" in normalized_input:
                        self.conversation_state["waiting_for_confirmation"] = True
                        return "¿Quizás quisiste decir 'Ascensor'? (Responde sí o no)"
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
                elif "escalera" in normalized_input:
                    self.conversation_state["equipment_type"] = "escalera"
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
                else:
                    return "Por favor, especifica si necesitas mantenimiento para Ascensor o Escalera eléctrica."
            
            # Selección de sector
            if not self.conversation_state["sector"]:
                sector_options = ["cabina", "parte mecánica", "sistema electrónico", "todo"]
                matched_sector = self.find_best_match(user_input, sector_options)
                
                if matched_sector:
                    self.conversation_state["sector"] = matched_sector
                    return "¿De qué marca es su equipo? (Puedes preguntar '¿qué marcas tienen?' para ver la lista)"
                else:
                    return "Por favor selecciona uno de estos sectores: Cabina, Parte mecánica, Sistema electrónico, Todo"
            
            # Consulta de marcas disponibles
            if "marcas" in normalized_input or "que marcas" in normalized_input:
                equipment_type = self.conversation_state["equipment_type"]
                if equipment_type == "ascensor":
                    brands = BUSINESS_INFO["elevator_brands"]
                else:
                    brands = BUSINESS_INFO["escalator_brands"]
                
                brands_text = ", ".join(brands)
                return f"Las marcas disponibles para {equipment_type} son: {brands_text}"
            
            # Selección de marca
            if not self.conversation_state["brand"]:
                # Verificar si el usuario quiere cambiar de contexto
                if "no" in normalized_input and ("ascensor" in normalized_input or "elevador" in normalized_input):
                    # Usuario quiere cambiar a ascensor
                    self.conversation_state["equipment_type"] = "ascensor"
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
                elif "no" in normalized_input and "escalera" in normalized_input:
                    # Usuario quiere cambiar a escalera
                    self.conversation_state["equipment_type"] = "escalera"
                    return "¿Qué sector requiere mantenimiento? (Cabina, Parte mecánica, Sistema electrónico, Todo)"
                
                equipment_type = self.conversation_state["equipment_type"]
                if equipment_type == "ascensor":
                    available_brands = BUSINESS_INFO["elevator_brands"]
                else:
                    available_brands = BUSINESS_INFO["escalator_brands"]
                
                matched_brand = self.find_best_match(user_input, available_brands)
                
                if matched_brand:
                    self.conversation_state["brand"] = matched_brand
                    # Verificar si necesita confirmación (para casos como "yaskawa" -> "Yaskawa")
                    if self.normalize_text(matched_brand) != self.normalize_text(user_input):
                        self.conversation_state["waiting_for_confirmation"] = True
                        return f"¿Te refieres a la marca {matched_brand}? (Responde sí o no)"
                    else:
                        return "¿Cuántos años de antigüedad tiene el equipo? (Por favor, ingrese un número entre 1 y 50)"
                else:
                    return f"Por favor selecciona una marca válida. Puedes preguntar '¿qué marcas tienen?' para ver la lista."
            
            # Edad del equipo
            if not self.conversation_state["age"]:
                age = self.validate_age(user_input)
                if age is not None:
                    self.conversation_state["age"] = age
                    return self.generate_price_quote()
                else:
                    return "Por favor ingresa un número válido entre 1 y 50 años."
            
            # Si llegamos aquí, ya tenemos todos los datos
            return self.generate_price_quote()
        
        # Si no se ha especificado el tipo de servicio, preguntar
        return "¿Qué tipo de servicio necesitas? (Mantenimiento o Modernización)"
    
    def handle_emergency(self, user_input: str) -> str:
        """Maneja las emergencias de ascensores atrapados"""
        response = "🚨 **EMERGENCIA - ASCENSOR ATRAPADO**\n\n"
        
        for step in BUSINESS_INFO["emergency_steps"]:
            response += f"{step}\n"
        
        response += f"\n📞 **CONTACTO INMEDIATO:**\n"
        response += f"• WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• Nuestro técnico llegará en máximo 15 minutos\n\n"
        response += f"⚠️ **NO INTENTES ABRIR LAS PUERTAS MANUALMENTE**\n"
        response += f"🔒 **MANTÉN LA CALMA** - Estamos en camino"
        
        return response
    
    def handle_brand_price_query(self, user_input: str) -> str:
        """Maneja consultas de precios por marca"""
        # Extraer marca del input
        normalized_input = self.normalize_text(user_input)
        
        # Buscar marca en el input
        found_brand = None
        for brand in BUSINESS_INFO["elevator_brands"]:
            if self.normalize_text(brand) in normalized_input:
                found_brand = brand
                break
        
        if found_brand:
            # Calcular precio base para la marca
            base_price = BUSINESS_INFO["maintenance_pricing"]["ascensor"]["by_brand"].get(found_brand, 1200)
            
            response = f"💰 **PRECIO REFERENCIAL - ASCENSOR {found_brand.upper()}**\n\n"
            response += f"• **Precio base:** S/. {base_price:,.2f} soles\n"
            response += f"• **Rango estimado:** S/. {base_price-200:,.2f} - S/. {base_price+300:,.2f} soles\n\n"
            response += f"💡 **Nota:** Este es un precio referencial. El costo final depende de:\n"
            response += f"• Edad del equipo\n"
            response += f"• Sector a mantener\n"
            response += f"• Estado actual del ascensor\n\n"
            response += f"📞 **Para cotización exacta contacta directamente:**\n"
            response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}\n"
            response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
            response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}"
            
            return response
        else:
            return "Por favor especifica la marca del ascensor para darte un precio referencial."
    
    def handle_recommendation_query(self, user_input: str) -> str:
        """Maneja consultas de recomendaciones de ascensores"""
        normalized_input = self.normalize_text(user_input)
        
        if "edificio" in normalized_input:
            rec = BUSINESS_INFO["recommendations"]["edificio"]
        elif "departamento" in normalized_input:
            rec = BUSINESS_INFO["recommendations"]["departamento"]
        else:
            # Recomendación general
            rec = BUSINESS_INFO["recommendations"]["edificio"]
        
        response = f"{rec['title']}\n\n"
        response += f"**Recomendación:** {rec['recommendation']}\n\n"
        response += f"**¿Por qué esta opción?**\n"
        
        for reason in rec["reasons"]:
            response += f"• {reason}\n"
        
        response += f"\n{rec['contact_info']}\n"
        response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}\n"
        response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}"
        
        return response
    
    def handle_disability_query(self) -> str:
        """Maneja consultas sobre soluciones para discapacidad"""
        rec = BUSINESS_INFO["recommendations"]["discapacidad"]
        
        response = f"{rec['title']}\n\n"
        response += f"**Solución recomendada:** {rec['recommendation']}\n\n"
        response += f"**Características:**\n"
        
        for reason in rec["reasons"]:
            response += f"• {reason}\n"
        
        response += f"\n{rec['contact_info']}\n"
        response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}\n"
        response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}"
        
        return response
    
    def handle_school_elevator_query(self) -> str:
        """Maneja consultas sobre ascensores para colegios"""
        rec = BUSINESS_INFO["recommendations"]["colegio"]
        
        response = f"{rec['title']}\n\n"
        response += f"**Recomendación:** {rec['recommendation']}\n\n"
        response += f"**Características especiales:**\n"
        
        for reason in rec["reasons"]:
            response += f"• {reason}\n"
        
        response += f"\n**Costo estimado:** S/. 15,000 - S/. 45,000 soles\n"
        response += f"*El precio varía según capacidad, pisos y especificaciones*\n\n"
        response += f"{rec['contact_info']}\n"
        response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}\n"
        response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}"
        
        return response
    
    def handle_escalator_modernization_query(self) -> str:
        """Maneja consultas sobre modernización de escaleras eléctricas"""
        pricing = BUSINESS_INFO["modernization_pricing"]["escalera"]
        
        response = "🏗️ **MODERNIZACIÓN DE ESCALERA ELÉCTRICA**\n\n"
        response += f"**Costos estimados:**\n"
        response += f"• **Modernización Básica:** ${pricing['basic']['usd_min']:,} - ${pricing['basic']['usd_max']:,} USD\n"
        response += f"• **Proyecto Completo:** ${pricing['complete']['usd_min']:,} - ${pricing['complete']['usd_max']:,} USD\n"
        response += f"• **En soles:** S/. {pricing['average_soles']['min']:,} - S/. {pricing['average_soles']['max']:,}\n\n"
        response += f"**Para cotización precisa contacta:**\n"
        response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}\n"
        response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}"
        
        return response
    
    def handle_elevator_modernization_query(self) -> str:
        """Maneja consultas sobre modernización de ascensores"""
        pricing = BUSINESS_INFO["modernization_pricing"]["ascensor"]
        
        response = "🏗️ **MODERNIZACIÓN DE ASCENSOR**\n\n"
        response += f"**Costos estimados:**\n"
        response += f"• **Modernización Básica:** ${pricing['basic']['usd_min']:,} - ${pricing['basic']['usd_max']:,} USD\n"
        response += f"• **Proyecto Completo:** ${pricing['complete']['usd_min']:,} - ${pricing['complete']['usd_max']:,} USD\n"
        response += f"• **En soles:** S/. {pricing['average_soles']['min']:,} - S/. {pricing['average_soles']['max']:,}\n\n"
        response += f"**Para cotización precisa contacta:**\n"
        response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}\n"
        response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}"
        
        return response
    
    def handle_technician_contact(self) -> str:
        """Maneja solicitudes de contacto con técnico"""
        response = "👨‍🔧 **CONTACTO CON TÉCNICO**\n\n"
        response += f"**Para contacto directo con nuestro técnico:**\n\n"
        response += f"📱 **WhatsApp:** {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"📞 **Teléfono:** {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"📧 **Email:** {BUSINESS_INFO['contact_email']}\n\n"
        response += f"⏰ **Disponibilidad:** 24/7 para emergencias\n"
        response += f"🚗 **Tiempo de respuesta:** Máximo 15 minutos"
        
        return response
    
    def handle_appointment_request(self) -> str:
        """Maneja solicitudes de agendar citas"""
        response = "📅 **AGENDAR MANTENIMIENTO PREVENTIVO**\n\n"
        response += f"**Para agendar tu mantenimiento:**\n\n"
        response += f"📱 **WhatsApp:** {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"📞 **Teléfono:** {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"📧 **Email:** {BUSINESS_INFO['contact_email']}\n\n"
        response += f"**Información que necesitamos:**\n"
        response += f"• Marca y modelo del ascensor\n"
        response += f"• Dirección del edificio\n"
        response += f"• Horario preferido\n"
        response += f"• Tipo de mantenimiento requerido"
        
        return response
    
    def handle_spare_parts_query(self, user_input: str) -> str:
        """Maneja consultas sobre repuestos específicos"""
        normalized_input = self.normalize_text(user_input)
        
        # Buscar categoría de repuesto
        found_category = None
        found_product = None
        
        # Buscar por categoría primero
        for category, products in BUSINESS_INFO["repuestos_pricing"].items():
            category_normalized = self.normalize_text(category)
            if category_normalized in normalized_input:
                found_category = category
                break
        
        # Si no se encontró categoría, buscar por producto específico
        if not found_category:
            for category, products in BUSINESS_INFO["repuestos_pricing"].items():
                for product_name in products.keys():
                    product_normalized = self.normalize_text(product_name)
                    # Buscar coincidencias parciales
                    if any(word in product_normalized for word in normalized_input.split()) or any(word in normalized_input for word in product_normalized.split()):
                        found_product = product_name
                        found_category = category
                        break
                if found_product:
                    break
        
        if found_product:
            # Producto específico encontrado
            product_info = BUSINESS_INFO["repuestos_pricing"][found_category][found_product]
            response = f"🔧 **REPUESTO: {found_product}**\n\n"
            response += f"**Descripción:** {product_info['desc']}\n"
            response += f"**Precio:** S/. {product_info['min']:,} - S/. {product_info['max']:,} soles\n\n"
            response += f"**Para compra directa contacta:**\n"
            response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
            response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
            response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}"
            
            return response
        elif found_category:
            # Categoría encontrada
            products = BUSINESS_INFO["repuestos_pricing"][found_category]
            response = f"🔧 **REPUESTOS - {found_category}**\n\n"
            
            for product_name, product_info in products.items():
                response += f"• **{product_name}:** S/. {product_info['min']:,} - S/. {product_info['max']:,} soles\n"
            
            response += f"\n**Para cotización específica contacta:**\n"
            response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
            response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
            response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}"
            
            return response
        else:
            # Lista general de categorías
            response = "🔧 **CATEGORÍAS DE REPUESTOS DISPONIBLES**\n\n"
            
            for category in BUSINESS_INFO["repuestos_pricing"].keys():
                response += f"• {category}\n"
            
            response += f"\n**Para consultar precios específicos contacta:**\n"
            response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
            response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
            response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}"
            
            return response
    
    def generate_price_quote(self) -> str:
        """Genera la cotización de precio final"""
        price = self.calculate_maintenance_price()
        if price == 0:
            return "Lo siento, no se pudo calcular el precio. Por favor, verifica que todos los datos sean correctos."
        
        equipment_type = self.conversation_state["equipment_type"]
        brand = self.conversation_state["brand"]
        sector = self.conversation_state["sector"]
        age = self.conversation_state["age"]
        
        # Formatear el tipo de equipo para mostrar
        equipment_display = "Ascensor" if equipment_type == "ascensor" else "Escalera eléctrica"
        
        quote = (
            f"El precio estimado para el mantenimiento de su {equipment_display} marca {brand}, "
            f"sectores {sector}, con {age} años de antigüedad es: S/. {price:,.2f} soles.\n\n"
            f"💡 {BUSINESS_INFO['maintenance_warranty']}\n\n"
            f"📞 Para más información o programar una visita, contáctanos:\n"
            f"• Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
            f"• Email: {BUSINESS_INFO['contact_email']}\n"
            f"• Horario: {BUSINESS_INFO['hours']}"
        )
        
        # Reiniciar conversación para la próxima consulta
        self.reset_conversation()
        
        return quote

    def handle_technical_support_query(self) -> str:
        """Maneja consultas sobre asistencia técnica"""
        response = "🛠️ **ASISTENCIA TÉCNICA**\n\n"
        response += f"**Nuestros servicios de asistencia técnica incluyen:**\n\n"
        response += f"• 🔧 **Diagnóstico técnico** gratuito\n"
        response += f"• 🚨 **Emergencias 24/7** - Respuesta en 15 minutos\n"
        response += f"• 📞 **Soporte telefónico** especializado\n"
        response += f"• 👨‍🔧 **Visitas técnicas** programadas\n"
        response += f"• 📋 **Reportes técnicos** detallados\n"
        response += f"• 🛡️ **Garantía** en todos los servicios\n\n"
        response += f"**Para solicitar asistencia técnica:**\n"
        response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}\n\n"
        response += f"⏰ **Disponibilidad:** 24/7 para emergencias"
        
        return response
    
    def handle_escalator_price_query(self) -> str:
        """Maneja consultas específicas sobre precios de escaleras eléctricas"""
        pricing = BUSINESS_INFO["maintenance_pricing"]["escalera"]
        
        response = "💰 **PRECIOS DE MANTENIMIENTO - ESCALERAS ELÉCTRICAS**\n\n"
        response += f"**Precio base:** S/. {pricing['base']:,} soles\n\n"
        response += f"**Precios por marca:**\n"
        for brand, price in pricing['by_brand'].items():
            response += f"• {brand}: S/. {price:,} soles\n"
        
        response += f"\n**Ajustes por sector:**\n"
        for sector, adjustment in pricing['sector_adjustment'].items():
            if adjustment > 0:
                response += f"• {sector.replace('_', ' ').title()}: +S/. {adjustment:,} soles\n"
        
        response += f"\n**Ajustes por antigüedad:**\n"
        for age_range in pricing['age_adjustment']:
            if age_range['adjustment'] > 0:
                response += f"• {age_range['min']}-{age_range['max']} años: +S/. {age_range['adjustment']:,} soles\n"
        
        response += f"\n**Para cotización personalizada contacta:**\n"
        response += f"• 📱 WhatsApp: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📞 Teléfono: {BUSINESS_INFO['contact_phone_primary']}\n"
        response += f"• 📧 Email: {BUSINESS_INFO['contact_email']}"
        
        return response

def main():
    """Función principal para ejecutar el chatbot"""
    chatbot = ElevatorChatbot()
    
    print("🤖 Chatbot de Mantenimiento de Ascensores y Escaleras Eléctricas")
    print("=" * 60)
    print("Escribe 'salir' para terminar la conversación")
    print("Escribe 'reiniciar' para comenzar una nueva consulta")
    print("-" * 60)
    
    while True:
        user_input = input("Usuario: ").strip()
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Bot: ¡Gracias por contactarnos! Que tengas un excelente día. 👋")
            break
        
        if user_input.lower() in ["reiniciar", "reset", "nuevo"]:
            chatbot.reset_conversation()
            print("Bot: Conversación reiniciada. ¿En qué puedo ayudarte? 😊")
            continue
        
        if not user_input:
            continue
        
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
        print("-" * 60)

if __name__ == "__main__":
    main() 