#!/usr/bin/python3.10

# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_talisman import Talisman, ALLOW_FROM

app = Flask(__name__)

talisman = Talisman(app)

@app.route('/')
def hello_world():
    return 'Prueba del hosting (usando Talisman)...'

@app.route('/decrypt')
def decrypt():
    return 'Ruta de desencriptado'

@app.route('/crypt')
def crypt():
    return 'Ruta de encriptado'

@app.route('/login')
def login():
    return 'Aqui ira el login de la aplicacion'




