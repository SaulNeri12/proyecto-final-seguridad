from app import db

class User(db.Model):

    __tablename__ = "user"

    # definimos el ID del usuario
    id = db.Column(db.Integer, primary_key=True)
    # definimos el nombre de usuario (Maximo 40 caracteres)
    username = db.Column(db.String(40), nullable=False, unique=True)
    # definimos el email de usuario (para tener datos importantes)
    email = db.Column(db.String(100), nullable=False, unique=True)
    # definimos la contrasena (Maximo 100 caracteres)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def register_user(username, email, password):
    '''Registra un usuario tras ingresar sus datos en el formulario de registro'''
    # se verifican los datos

    # usuario a insertar
    user = User(username, email, password)
    
    # indica que se guardara el usuario en la base de datos
    db.session.add(user)

    # indica que se confirme la peticion (se guarda en la base de datos)
    db.session.commit()


def login_user(username, password):
    ''' Verifica si el usuario con dicho nombre existe y si la contrasena coincide lo deja ingresar
        a la funcionalidad principal de la aplicacion
    '''
    # verifica si existe en la base de datos un usuario con dicho nombre de usuario

    # verifica si la contrasena corresponde con la del usuario almacenado en la base de datos
    pass


if __name__ == "__main__":
    print("[!] Creando base de datos...")
    db.create_all()
    print("[*] Base de datos creada... Funcionando..,")
