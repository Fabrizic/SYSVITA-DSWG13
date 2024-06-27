from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.puntuacion import Puntuacion

"""CREATE TABLE Puntuacion (
    puntuacionid SERIAL PRIMARY KEY,
    testid INT NOT NULL,
    rango_inferior INT NOT NULL,
    rango_superior INT NOT NULL,
    diagnostico VARCHAR(255) NOT NULL,
    FOREIGN KEY (testid) REFERENCES Test(testid)
);
0"""


