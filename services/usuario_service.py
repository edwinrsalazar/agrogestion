from models.usuario_model import get_usuario_by_username, create_usuario, get_all_usuarios, get_usuario_by_id, update_usuario, delete_usuario
from werkzeug.security import generate_password_hash, check_password_hash

def validar_usuario(username, password):
    user = get_usuario_by_username(username)

    if user and check_password_hash(user['password'], password):
        return user

    return None

def registrar_usuario(nombre, documento, telefono, correo, username, password, rol):
    if not username or not password:
        return None

    password_hash = generate_password_hash(password)

    create_usuario(nombre, documento, telefono, correo, username, password_hash, rol)
    return True


def listar_usuarios():
    return get_all_usuarios()

def obtener_usuario(id):
    return get_usuario_by_id(id)


def editar_usuario(id, username, password, rol):
    password_hash = generate_password_hash(password)
    update_usuario(id, username, password_hash, rol)
    
def eliminar_usuario(id):
    delete_usuario(id)