#!/usr/bin/python3.10

# framework para servidor web
from flask import Flask
# libreria que se encarga de prevenir los ataques de
# cabeceras HTTP mas comunes
from flask_talisman import Talisman, ALLOW_FROM
# Servicio de ORM para Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configura la URL de la base de datos (en este caso MySQL)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://neri6502:cryptocucumber6502@neri6502.mysql.pythonanywhere-services.com/neri6502$proyecto-final"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# instancia del cursor de la base de datos
db = SQLAlchemy(app)



# Talisman para definir comportamientos especificos en cada ruta...
talisman = Talisman(app)

import views

if __name__ == "__main__":
    app.run()

