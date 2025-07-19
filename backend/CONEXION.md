# 🔗 Conexión Backend-Frontend

## 📋 Resumen

Este documento explica cómo conectar el backend del chatbot con el frontend HTML/JavaScript.

## 🚀 Pasos para la Conexión

### 1. Instalar Dependencias

```bash
cd backend
pip install -r requirements.txt
```

### 2. Ejecutar el Servidor Backend

```bash
# Opción 1: Usando el script automático
python run_server.py

# Opción 2: Directamente
python app.py
```

El servidor se ejecutará en: `http://localhost:5000`

### 3. Verificar que el Frontend esté Configurado

El archivo `js/main.js` ya está configurado para conectarse al backend:

```javascript
export async function getChatbotResponse(message) {
  const res = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: message,
      mantenimiento_flujo: flujoMantenimiento,
    }),
    credentials: "include",
  });
  const data = await res.json();
  // ... manejo de respuesta
  return data.response;
}
```

## 🔧 Endpoints Disponibles

### POST /chat

- **Propósito**: Procesar mensajes del usuario
- **Body**: `{ "message": "texto del usuario", "mantenimiento_flujo": {...} }`
- **Respuesta**: `{ "response": "respuesta del bot", "mantenimiento_flujo": {...} }`

### GET /health

- **Propósito**: Verificar estado del servidor
- **Respuesta**: `{ "status": "ok", "message": "Chatbot funcionando correctamente" }`

### POST /reset

- **Propósito**: Reiniciar la conversación
- **Respuesta**: `{ "message": "Conversación reiniciada" }`

### GET /catalogo

- **Propósito**: Obtener catálogo de repuestos
- **Respuesta**: Catálogo completo en formato JSON

## 🧪 Pruebas de Conexión

### 1. Verificar Servidor

```bash
curl http://localhost:5000/health
```

### 2. Probar Chat

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hola"}'
```

## 🔍 Solución de Problemas

### Error: "CORS policy"

- **Causa**: El navegador bloquea peticiones desde el frontend
- **Solución**: El servidor ya tiene CORS configurado para los orígenes comunes

### Error: "Connection refused"

- **Causa**: El servidor no está ejecutándose
- **Solución**: Verificar que el servidor esté corriendo en el puerto 5000

### Error: "Module not found"

- **Causa**: Dependencias no instaladas
- **Solución**: Ejecutar `pip install -r requirements.txt`

## 📱 Uso en el Frontend

El archivo `chat.html` ya está configurado para usar la función `getChatbotResponse`:

```javascript
// En chat.html
import { getChatbotResponse } from "./js/main.js";

// Uso
const aiResponse = await getChatbotResponse(message);
displayMessage(aiResponse, false, null, true);
```

## 🎯 Estado de la Conversación

El sistema mantiene el estado de la conversación (flujo de mantenimiento) automáticamente:

1. **Frontend**: Guarda el estado en `localStorage`
2. **Backend**: Recibe y restaura el estado en cada petición
3. **Sincronización**: El estado se mantiene sincronizado entre frontend y backend

## ✅ Verificación Final

1. ✅ Servidor ejecutándose en `http://localhost:5000`
2. ✅ Frontend accesible (archivo HTML)
3. ✅ CORS configurado correctamente
4. ✅ Endpoints respondiendo
5. ✅ Chat funcionando

¡La conexión está lista! 🎉
