# Proyecto de Pruebas de Caso de Uso de Respuestas de Usuarios para SISVITA

SISVITA es una página web de ayuda psicológica que permite a los usuarios realizar un test de ansiedad. Este proyecto es un caso de uso para realizar pruebas en el sistema de test de ansiedad de SISVITA.

# Integrantes

- Leiva Misari, Fabrizio
- Quispe Rueda, Diego
- Duran Solis, Yago

## Cómo usar

Para utilizar este proyecto, necesitarás enviar una solicitud HTTP con un cuerpo JSON. Aquí tienes un ejemplo de cómo debería ser el formato JSON:

```json
{
    "usuario_id": 4,
    "nombre": "Yago",
    "email": "yago.solis@example.com",
    "edad": 21,
    "respuestas": [
        {
            "pregunta_id": 1,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 2,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 3,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 4,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 5,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 6,
            "respuesta_id": 3
        },{
            "pregunta_id": 7,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 8,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 9,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 10,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 11,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 12,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 13,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 14,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 15,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 16,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 17,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 18,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 19,
            "respuesta_id": 3
        },
        {
            "pregunta_id": 20,
            "respuesta_id": 3
        }
    ]
}
```

Cada objeto en el array `respuestas` representa una respuesta a una pregunta del test de ansiedad. `pregunta_id` es el ID de la pregunta y `respuesta_id` es el ID de la respuesta seleccionada por el usuario.

## Rutas

- `POST /respuestas_usuarios`: Crea nuevas respuestas de un usuario.
- `GET /respuestas_usuarios`: Obtiene las respuestas de un usuario.
- `PUT /respuestas_usuarios`: Actualiza las respuestas de un usuario.
- `DELETE /respuestas_usuarios`: Elimina las respuestas de un usuario.

## Requisitos

- Python 3.6+
- Flask
- SQLAlchemy

## Instalación

1. Clona este repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta el servidor con `python app.py`.
