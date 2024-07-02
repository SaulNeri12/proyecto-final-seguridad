from app import db

from hashlib import sha512

class SignUpError(Exception):
    def __init__(self, message):            
        self.message = message

class LogInError(Exception):
    def __init__(self, message):            
        self.message = message

class User(db.Model):
    __tablename__ = "user"

    # definimos el ID del usuario
    id = db.Column(db.Integer, primary_key=True)
    # definimos el nombre de usuario (Maximo 40 caracteres)
    username = db.Column(db.String(32), nullable=False, unique=True)
    # definimos el email de usuario (para tener datos importantes)
    email = db.Column(db.String(150), nullable=False, unique=True)
    # definimos la contrasena (Maximo 100 caracteres)
    password = db.Column(db.String(158), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def register_user(username, email, password):
    '''Registra un usuario tras ingresar sus datos en el formulario de registro'''
    # se verifican los datos

    # se hashean los campos
    email_hash = sha512(email.encode()).hexdigest()
    password_hash = sha512(password.encode()).hexdigest()

    # usuario a insertar
    user = User(username, email_hash, password_hash)
    
    # indica que se guardara el usuario en la base de datos
    db.session.add(user)

    # indica que se confirme la peticion (se guarda en la base de datos)
    db.session.commit()


def user_exists(username, email) -> bool:
    '''Verifica si ya existe un usuario con el correo o el usuario dado'''
    
    # convertir el email dado a sha512
    email_hash = sha512(email.encode()).hexdigest()
    user = User.query.filter_by(email=email_hash).first()
   
    if user == None:
        user = User.query.filter_by(username=username).first()

    return (user != None)


def login_user(username, password):
    ''' Verifica si el usuario con dicho nombre existe y si la contraseña coincide lo deja ingresar
        a la funcionalidad principal de la aplicacion
    '''
    # verifica si existe en la base de datos un usuario con dicho nombre de usuario
    user = User.query.filter_by(username=username).first()
    
    if user == None:
        raise LogInError("No existe un usuario registrado con el nombre dado")
    else:
        password_hash = sha512(password.encode()).hexdigest()
        if password_hash != user.password:
            raise LogInError("La contraseña es incorrecta")


if __name__ == "__main__":
    print("[!] Creando base de datos...")
    db.create_all()
    print("[*] Base de datos creada... Funcionando..,")



