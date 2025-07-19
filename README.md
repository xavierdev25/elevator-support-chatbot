# 🏢 Chatbot Demo - Empresa de Ascensores

## 📋 Descripción

Este proyecto es una aplicación web completa que simula el sitio web y sistema de atención al cliente de una empresa de ascensores. Incluye un chatbot inteligente que puede asistir a los usuarios con consultas sobre mantenimiento, cotizaciones y catálogo de repuestos.

## ✨ Características Principales

### 🌐 Sitio Web Corporativo

- **Diseño moderno y responsivo** con Tailwind CSS
- **Animaciones y efectos visuales** con AOS (Animate On Scroll)
- **Navegación fluida** con scroll suave
- **Secciones completas**: Inicio, Video promocional, Productos, Servicios, Clientes, Valores y Contacto
- **Interfaz de glassmorphism** con efectos de transparencia y blur

### 🤖 Chatbot Inteligente

- **Asistencia técnica especializada** en ascensores
- **Solicitud de cotizaciones** automatizada
- **Catálogo de repuestos** integrado
- **Flujo de conversación contextual** que mantiene el estado
- **Respuestas personalizadas** basadas en el contexto del usuario

### 🔐 Sistema de Autenticación

- **Registro e inicio de sesión** con Firebase Authentication
- **Recuperación de contraseñas** por email
- **Interfaz de usuario moderna** con animaciones 3D
- **Validación de formularios** en tiempo real

### 🚀 Backend API

- **Servidor Flask** con endpoints RESTful
- **Procesamiento de lenguaje natural** para el chatbot
- **CORS configurado** para desarrollo
- **Logging y manejo de errores** robusto

## 🛠️ Tecnologías Utilizadas

### Frontend

- **HTML5** - Estructura semántica
- **CSS3** - Estilos y animaciones
- **JavaScript (ES6+)** - Interactividad y lógica
- **Tailwind CSS** - Framework de utilidades CSS
- **Font Awesome** - Iconografía
- **AOS** - Animaciones al hacer scroll

### Backend

- **Python 3.x** - Lenguaje principal
- **Flask** - Framework web
- **Flask-CORS** - Manejo de CORS
- **Procesamiento de lenguaje natural** - Para el chatbot

### Base de Datos y Autenticación

- **Firebase Authentication** - Sistema de autenticación
- **Firebase Firestore** - Base de datos en tiempo real
- **Firebase Realtime Database** - Sincronización en tiempo real

### Herramientas de Desarrollo

- **Git** - Control de versiones
- **npm/yarn** - Gestión de dependencias (si aplica)

## 📁 Estructura del Proyecto

```
chatbot-demo/
├── 📄 index.html              # Página principal del sitio web
├── 📄 chat.html               # Interfaz del chatbot
├── 📄 login.html              # Sistema de autenticación
├── 📄 IA.html                 # Página adicional de IA
├── 📄 style.css               # Estilos globales
├── 📄 catalogo_repuestoAV.pdf # Catálogo de repuestos
├── 📁 js/                     # Scripts de JavaScript
│   ├── 📄 main.js             # Lógica principal del chatbot
│   ├── 📄 firebase-config.js  # Configuración de Firebase
│   └── 📄 spellcheck.js       # Corrección ortográfica
├── 📁 backend/                # Servidor y lógica del backend
│   ├── 📄 app.py              # Servidor Flask principal
│   ├── 📄 chatbot.py          # Lógica del chatbot
│   ├── 📄 business_info.py    # Información del negocio
│   ├── 📄 requirements.txt    # Dependencias de Python
│   ├── 📄 start_server.sh     # Script de inicio del servidor
│   └── 📄 CONEXION.md         # Documentación de conexión
└── 📄 .gitignore              # Archivos a ignorar en Git
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- **Python 3.8+** instalado
- **Node.js** (opcional, para herramientas de desarrollo)
- **Git** para clonar el repositorio

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd chatbot-demo
```

### 2. Configurar el Backend

#### Instalar dependencias de Python

```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Configurar Firebase

1. Crear un proyecto en [Firebase Console](https://console.firebase.google.com/)
2. Habilitar Authentication y Firestore
3. Obtener las credenciales de configuración
4. Actualizar `js/firebase-config.js` con tus credenciales

### 3. Iniciar el Servidor Backend

```bash
cd backend
python app.py
```

El servidor estará disponible en: `http://localhost:5000`

### 4. Abrir el Frontend

Simplemente abre `index.html` en tu navegador o usa un servidor local:

```bash
# Con Python
python -m http.server 8000

# Con Node.js (si tienes http-server instalado)
npx http-server
```

## 🔧 Configuración de Firebase

### 1. Crear Proyecto Firebase

1. Ve a [Firebase Console](https://console.firebase.google.com/)
2. Crea un nuevo proyecto
3. Habilita Authentication con email/password
4. Crea una base de datos Firestore

### 2. Configurar Credenciales

Actualiza el archivo `js/firebase-config.js`:

```javascript
const firebaseConfig = {
  apiKey: "tu-api-key",
  authDomain: "tu-proyecto.firebaseapp.com",
  projectId: "tu-proyecto",
  storageBucket: "tu-proyecto.firebasestorage.app",
  messagingSenderId: "tu-sender-id",
  appId: "tu-app-id",
  measurementId: "tu-measurement-id",
};
```

## 📡 Endpoints de la API

### POST `/chat`

Procesa mensajes del chatbot

```json
{
  "message": "Mensaje del usuario",
  "mantenimiento_flujo": "estado_actual"
}
```

### GET `/health`

Verifica el estado del servidor

```json
{
  "status": "ok",
  "message": "Chatbot funcionando correctamente"
}
```

### POST `/reset`

Reinicia la conversación del chatbot

### GET `/catalogo`

Obtiene el catálogo de repuestos

## 🎯 Funcionalidades del Chatbot

### Asistencia Técnica

- Diagnóstico de problemas comunes
- Guías de mantenimiento preventivo
- Solución de emergencias
- Programación de visitas técnicas

### Cotizaciones

- Cálculo automático de precios
- Diferentes tipos de servicios
- Descuentos especiales
- Generación de propuestas

### Catálogo de Repuestos

- Búsqueda de componentes
- Especificaciones técnicas
- Precios actualizados
- Disponibilidad en stock

## 🎨 Características de la UI/UX

### Diseño Responsivo

- Adaptable a móviles, tablets y desktop
- Navegación optimizada para cada dispositivo
- Botones y elementos táctiles apropiados

### Efectos Visuales

- Animaciones suaves y profesionales
- Efectos de hover y transiciones
- Gradientes y sombras modernas
- Partículas animadas en el hero

### Accesibilidad

- Navegación por teclado
- Contraste adecuado
- Textos legibles
- Iconografía descriptiva

## 🔒 Seguridad

### Autenticación

- Validación de email y contraseña
- Encriptación de contraseñas
- Tokens de sesión seguros
- Recuperación de contraseñas

### API

- Validación de entrada
- Manejo de errores
- CORS configurado
- Rate limiting (recomendado para producción)

## 🚀 Despliegue

### Opciones de Hosting

#### Frontend

- **GitHub Pages** - Gratuito para sitios estáticos
- **Netlify** - Despliegue automático desde Git
- **Vercel** - Optimizado para aplicaciones web
- **Firebase Hosting** - Integración con Firebase

#### Backend

- **Heroku** - Fácil despliegue de Python
- **Railway** - Alternativa moderna a Heroku
- **Google Cloud Run** - Escalable y eficiente
- **AWS Lambda** - Serverless

### Variables de Entorno

```bash
# Firebase
FIREBASE_API_KEY=tu-api-key
FIREBASE_PROJECT_ID=tu-proyecto

# Flask
FLASK_ENV=production
FLASK_SECRET_KEY=tu-secret-key
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Tu Nombre** - _Desarrollo inicial_ - [TuGitHub](https://github.com/tuusuario)

## 🙏 Agradecimientos

- **Tailwind CSS** por el framework de utilidades
- **Firebase** por la infraestructura de backend
- **Font Awesome** por los iconos
- **AOS** por las animaciones de scroll

## 📞 Soporte

Si tienes alguna pregunta o necesitas ayuda:

- 📧 Email: tu-email@ejemplo.com
- 💬 Issues: [GitHub Issues](https://github.com/tuusuario/chatbot-demo/issues)
- 📖 Documentación: [Wiki del proyecto](https://github.com/tuusuario/chatbot-demo/wiki)

---

⭐ **¡No olvides darle una estrella al proyecto si te gustó!**
