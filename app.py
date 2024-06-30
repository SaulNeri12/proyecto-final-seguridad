#!/usr/bin/python3.10

# framework para servidor web
from flask import Flask
# libreria que se encarga de prevenir los ataques de
# cabeceras HTTP mas comunes
from flask_talisman import Talisman, ALLOW_FROM
# Servicio de ORM para Flask
from flask_sqlalchemy import SQLAlchemy
# carga la libreria para acceder al archivo de variables de la aplicacion
from dotenv import load_dotenv

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
# se carga el archivo de variables de la aplicacion...
load_dotenv(os.path.join(BASEDIR, '.env'))


app = Flask(__name__)

# configura la URL de la base de datos (en este caso MySQL)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqldb://neri6502:cryptocucumber6502@neri6502.mysql.pythonanywhere-services.com/neri6502$proyecto-final' 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 10 # conexiones a base de datos simultaneas
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 3600  # 1 hora maximo por conexion
app.config['WTF_CSRF_ENABLED'] = True

# se carga la clave secreta de la aplicacion
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")

# configuracion del captcha
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = os.getenv('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.getenv('RECAPTCHA_PRIVATE_KEY')
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

# instancia del cursor de la base de datos
db = SQLAlchemy(app)

# Configuración de CSP para permitir scripts de 'self' y 'https://www.google.com'
# permite que se inserte codigo JavaScript de estas fuentes solamente, fuentes
# las cuales son "confiables" para nuestra aplicacion ya que nos permiten que se
# muestre el reCAPTCHA
csp = {
    'default-src': [
        '\'self\''
    ],
    'script-src': [
        '\'self\'',
        'https://www.google.com',
        'https://www.gstatic.com'
    ],
    'frame-src': [
        '\'self\'',
        'https://www.google.com'
    ]
}

Talisman(app, content_security_policy=csp)

# Talisman para definir comportamientos especificos en cada ruta...
talisman = Talisman(app)

import views

if __name__ == "__main__":
    app.run()

