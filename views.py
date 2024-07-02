
from flask import render_template, request, flash, redirect
from models import *
from app import app

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Email, Length, InputRequired

class LogInForm(FlaskForm):
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
    recaptcha = RecaptchaField()

    submit = SubmitField('Iniciar Sesion')


class SignUpForm(FlaskForm):
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
    '''
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
    '''
    recaptcha = RecaptchaField()

    submit = SubmitField('Crear Cuenta')


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
    form = LogInForm()

    if form.validate_on_submit():
        try:
            login_user(form.username.data, form.password.data)
            return redirect('crypt')
        except LogInError as e:
            flash(e.message, "error")

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #register_user("pedro", "pedro123@gmail,com", "shesh")

    form = SignUpForm()

    if form.validate_on_submit():
        if user_exists(form.username.data, form.email.data):
            flash("Ya existe un usuario con el correo o nombre de usuario dado", "error")
        else:
            # cargamos los datos del formulario...
            username = form.username.data
            email = form.username.data
            password = form.password.data
            # registramos el usuario en la base de datos
            register_user(username, email, password)
            return redirect('login')
    else:
        errors = {}
        for field, errors_list in form.errors.items():
            errors[field] = ', '.join(errors_list)
            for error in errors_list:
                print(f"Error en el campo '{field}': {error}")

    return render_template('signup.html', form=form)


@app.route('/test-create-user', methods=['GET'])
def test_create_user():
    register_user("pedro", "pedro123@gmail,com", "shesh")
    return 'Se creo un usuario de prueba...'





















