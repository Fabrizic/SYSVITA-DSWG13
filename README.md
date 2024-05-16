Creación de BD :
CREATE TABLE Usuarios (
    usuario_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Tests (
    test_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion VARCHAR(100)
);

CREATE TABLE Preguntas (
    pregunta_id SERIAL PRIMARY KEY,
    test_id INT REFERENCES Tests(test_id) ON DELETE CASCADE,
    texto_pregunta VARCHAR(100)
);

CREATE TABLE Respuestas (
    respuesta_id SERIAL PRIMARY KEY,
    pregunta_id INT REFERENCES Preguntas(pregunta_id) ON DELETE CASCADE,
    texto_respuesta VARCHAR(100)
);

CREATE TABLE Respuestas_Usuarios (
    respuesta_usuario_id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    pregunta_id INT REFERENCES Preguntas(pregunta_id) ON DELETE CASCADE,
    respuesta_id INT REFERENCES Respuestas(respuesta_id) ON DELETE CASCADE,
)

INSERT INTO Preguntas (test_id, texto_pregunta) VALUES
(1, 'Me siento más nervioso y ansioso que de costumbre.'),
(1, 'Siento miedo sin razón aparente.'),
(1, 'Me asusto fácilmente o tengo sobresaltos.'),
(1, 'Me siento tembloroso o inestable.'),
(1, 'Tengo dificultades para dormir.'),
(1, 'Me siento cansado o débil.'),
(1, 'Me siento triste o deprimido.'),
(1, 'Me siento inquieto y no puedo estar quieto.'),
(1, 'Siento mareos o aturdimiento.'),
(1, 'Tengo palpitaciones o latidos rápidos del corazón.'),
(1, 'Siento dolor o malestar en el pecho.'),
(1, 'Tengo problemas estomacales o indigestión.'),
(1, 'Tengo ganas de orinar con frecuencia.'),
(1, 'Tengo dificultad para respirar.'),
(1, 'Tengo sofocos o escalofríos.'),
(1, 'Siento adormecimiento u hormigueo en partes del cuerpo.'),
(1, 'Me siento tenso y con músculos rígidos.'),
(1, 'Tengo miedo de que algo terrible me pase.'),
(1, 'Siento que no puedo controlar mi preocupación.'),
(1, 'Tengo problemas para concentrarme o recordar cosas.');

INSERT INTO Respuestas (pregunta_id, texto_respuesta, nivel_intensidad) VALUES
(1, 'Nunca o casi nunca'),
(1, 'A veces'),
(1, 'Con frecuencia'),
(1, 'Siempre o casi siempre'),
(2, 'Nunca o casi nunca'),
(2, 'A veces'),
(2, 'Con frecuencia'),
(2, 'Siempre o casi siempre'),
(3, 'Nunca o casi nunca'),
(3, 'A veces'),
(3, 'Con frecuencia'),
(3, 'Siempre o casi siempre'),
(4, 'Nunca o casi nunca'),
(4, 'A veces'),
(4, 'Con frecuencia'),
(4, 'Siempre o casi siempre'),
(5, 'Nunca o casi nunca'),
(5, 'A veces'),
(5, 'Con frecuencia'),
(5, 'Siempre o casi siempre'),
(6, 'Nunca o casi nunca'),
(6, 'A veces'),
(6, 'Con frecuencia'),
(6, 'Siempre o casi siempre'),
(7, 'Nunca o casi nunca'),
(7, 'A veces'),
(7, 'Con frecuencia'),
(7, 'Siempre o casi siempre'),
(8, 'Nunca o casi nunca'),
(8, 'A veces'),
(8, 'Con frecuencia'),
(8, 'Siempre o casi siempre'),
(9, 'Nunca o casi nunca'),
(9, 'A veces'),
(9, 'Con frecuencia'),
(9, 'Siempre o casi siempre'),
(10, 'Nunca o casi nunca'),
(10, 'A veces'),
(10, 'Con frecuencia'),
(10, 'Siempre o casi siempre'),
(11, 'Nunca o casi nunca'),
(11, 'A veces'),
(11, 'Con frecuencia'),
(11, 'Siempre o casi siempre'),
(12, 'Nunca o casi nunca'),
(12, 'A veces'),
(12, 'Con frecuencia'),
(12, 'Siempre o casi siempre'),
(13, 'Nunca o casi nunca'),
(13, 'A veces'),
(13, 'Con frecuencia'),
(13, 'Siempre o casi siempre'),
(14, 'Nunca o casi nunca'),
(14, 'A veces'),
(14, 'Con frecuencia'),
(14, 'Siempre o casi siempre'),
(15, 'Nunca o casi nunca'),
(15, 'A veces'),
(15, 'Con frecuencia'),
(15, 'Siempre o casi siempre'),
(16, 'Nunca o casi nunca'),
(16, 'A veces'),
(16, 'Con frecuencia'),
(16, 'Siempre o casi siempre'),
(17, 'Nunca o casi nunca'),
(17, 'A veces'),
(17, 'Con frecuencia'),
(17, 'Siempre o casi siempre'),
(18, 'Nunca o casi nunca'),
(18, 'A veces'),
(18, 'Con frecuencia'),
(18, 'Siempre o casi siempre'),
(19, 'Nunca o casi nunca'),
(19, 'A veces'),
(19, 'Con frecuencia'),
(19, 'Siempre o casi siempre'),
(20, 'Nunca o casi nunca'),
(20, 'A veces'),
(20, 'Con frecuencia'),
(20, 'Siempre o casi siempre');

INSERT INTO Respuestas_Usuarios (usuario_id, pregunta_id, respuesta_id) VALUES
(1, 1, 2),
(1, 2, 3),
(1, 3, 1),
(1, 4, 2),
(1, 5, 3),
(1, 6, 4),
(1, 7, 2),
(1, 8, 3),
(1, 9, 4),
(1, 10, 1),
(1, 11, 2),
(1, 12, 3),
(1, 13, 1),
(1, 14, 4),
(1, 15, 2),
(1, 16, 3),
(1, 17, 4),
(1, 18, 2),
(1, 19, 3),
(1, 20, 4),

(2, 1, 3),
(2, 2, 2),
(2, 3, 4),
(2, 4, 1),
(2, 5, 3),
(2, 6, 2),
(2, 7, 4),
(2, 8, 1),
(2, 9, 3),
(2, 10, 2),
(2, 11, 4),
(2, 12, 1),
(2, 13, 3),
(2, 14, 2),
(2, 15, 4),
(2, 16, 1),
(2, 17, 3),
(2, 18, 2),
(2, 19, 3),
(2, 20, 1);

Probar POST:

{
    "usuario_id": 6,
    "nombre": "Yago",
    "email": "yago.solis@example.com",
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

Probar PUT(Update)
{
    "usuario_id": 1,
    "nombre": "Fabrizio Leiva",
    "email": "fabrizio.leiva@example.com",
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