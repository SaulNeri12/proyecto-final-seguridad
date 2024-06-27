
from models import User, register_user
from app import app

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

@app.route('/signup', methods=['POST'])
def signup():
    register_user("pedro", "pedro123@gmail,com", "shesh")
    return 'Aqui ira el login de la aplicacion'

@app.route('/test-create-user', methods=['GET'])
def test_create_user():
    register_user("pedro", "pedro123@gmail,com", "shesh")
    return 'Se creo un usuario de prueba...'


