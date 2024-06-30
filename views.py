
from flask import render_template, request
from models import User, register_user
from app import app

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import Email, Length, InputRequired

print("[*] Flask WTF funcionando!!!")

class SignupForm(FlaskForm):
    username = StringField('Nombre de usuario', 
        [
            InputRequired(), 
            Length(
                min=8, 
                max=32, 
                message='El nombre de usuario debe tener al menos 8 caracteres y no pasar de 32 caracteres'
            )
        ]
    )
    email = EmailField('Correo electronico', 
        [
            InputRequired(),
            Email(message='El correo electronico dado es incorrecto'),
            Length(
                max=320,
                message='El correo electronico dado es demasiado largo'
            )
        ]
    )
    password = PasswordField('Contrasena',
        [
            InputRequired(),
            Length(
                min=8,
                max=32,
                message='La contrasena debe contener al menos 8 caracteres y maximo de 32'
            )
        ]
    )
    confirm_password = PasswordField('Confirmar Contrasena',
        [
            InputRequired(),
            Length(
                min=8,
                max=32,
                message='La contrasena debe contener al menos 8 caracteres y maximo de 32'
            ),
        ]    
    )
    recaptcha = RecaptchaField()



@app.route('/')
@app.route('/home')
@app.route('/inicio')
def home():
    return render_template('home.html')

@app.route('/decrypt')
def decrypt():
    return 'Ruta de desencriptado'

@app.route('/crypt')
def crypt():
    return 'Ruta de encriptado'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print("post!!!!")

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #register_user("pedro", "pedro123@gmail,com", "shesh")

    form = SignupForm()

    if request.method == "POST":
        print("POST SIGNUP!!!!")

    return render_template('signup.html', form=form)


@app.route('/test-create-user', methods=['GET'])
def test_create_user():
    register_user("pedro", "pedro123@gmail,com", "shesh")
    return 'Se creo un usuario de prueba...'


