# Fichero donde importamos todos los ficheros del paquete y llamamos a la instancia app
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import modelo
from app import index
from app import mvt



