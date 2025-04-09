# Documentación de la API del Backend del ChatBot

## Descripción General
Texto descriptivo aquí, incluir propósito general del backend...

## Arquitectura
Detalles de la arquitectura aquí...

## Integración con IA
Explicación del sistema RAG y cómo se integra con GPT-4o Mini...

## Modelo de Datos
Descripción de las entidades y sus relaciones...

## Endpoints de la API

# Autenticación

- POST /api/users/register - Registro de nuevos usuarios
- POST /api/users/login - Autenticación de usuarios

# Gestión de Usuarios

- GET /api/users/{id} - Obtener información de un usuario específico
- PUT /api/users/{id} - Actualizar información de usuario
- DELETE /api/users/{id} - Eliminar usuario (solo administradores)
- GET /api/users - Listar todos los usuarios (solo administradores)
- POST /api/users/{id}/role - Cambiar rol de usuario (solo administradores)

# Gestión Documental

- POST /api/documents - Subir un nuevo documento
- GET /api/documents - Listar todos los documentos disponibles para el usuario
- GET /api/documents/{id} - Obtener información de un documento específico
- DELETE /api/documents/{id} - Eliminar un documento
- GET /api/documents/search - Buscar documentos por título o contenido
- POST /api/documents/share - Compartir documento con usuarios específicos
- GET /api/documents/shared - Listar documentos compartidos con el usuario
- POST /api/documents/{id}/users - Vincular un documento a usuarios específicos
- GET /api/documents/{id}/users - Listar usuarios con acceso a un documento
- DELETE /api/documents/{id}/users/{user_id} - Eliminar acceso de un usuario a un documento

# Chat

- POST /api/chats - Crear un nuevo chat
- GET /api/chats - Listar todos los chats del usuario
- GET /api/chats/{id} - Obtener información de un chat específico
- PUT /api/chats/{id} - Actualizar información de un chat
- DELETE /api/chats/{id} - Eliminar un chat
- POST /api/chats/{id}/messages - Enviar un mensaje al chatbot
- GET /api/chats/{id}/messages - Obtener todos los mensajes de un chat
- DELETE /api/chats/{id}/messages/{message_id} - Eliminar un mensaje específico

# Notificaciones

- POST /api/notifications - Crear una nueva notificación (administradores)
- GET /api/notifications - Obtener notificaciones del usuario
- PUT /api/notifications/{id}/read - Marcar notificación como leída


## Configuración y Despliegue
Instrucciones para configurar y ejecutar el backend...

## Seguridad
Medidas de seguridad implementadas en la API...