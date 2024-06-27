
from flask import render_template, request
from models import User, register_user
from app import app

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
    
    if request.method == "POST":
        print("POST SIGNUP!!!!")

    return render_template('signup.html')


@app.route('/test-create-user', methods=['GET'])
def test_create_user():
    register_user("pedro", "pedro123@gmail,com", "shesh")
    return 'Se creo un usuario de prueba...'


