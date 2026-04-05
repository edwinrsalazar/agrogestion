from models.usuario_model import (
    get_usuario_by_username,
    create_usuario,
    get_all_usuarios,
    get_usuario_by_id,
    update_usuario,
    delete_usuario,
    get_db_connection
)
from werkzeug.security import generate_password_hash, check_password_hash


# 🔐 VALIDAR LOGIN
def validar_usuario(username, password):
    user = get_usuario_by_username(username)

    if user and check_password_hash(user['password'], password):
        return user

    return None


# 🧑‍💼 REGISTRAR USUARIO
def registrar_usuario(nombre, documento, telefono, correo, username, password, rol):
    if not username or not password:
        return None

    password_hash = generate_password_hash(password)

    create_usuario(nombre, documento, telefono, correo, username, password_hash, rol)
    return True


# 📋 LISTAR
def listar_usuarios():
    return get_all_usuarios()


# 🔍 OBTENER
def obtener_usuario(id):
    return get_usuario_by_id(id)


# ✏️ EDITAR (CORREGIDO 🔥)
def editar_usuario(id, nombre, documento, telefono, correo, username, password, rol):
    conexion = get_db_connection()
    cursor = conexion.cursor()

    # 🔥 SI HAY CONTRASEÑA → ENCRIPTAR
    if password:
        password_hash = generate_password_hash(password)

        cursor.execute("""
            UPDATE usuarios 
            SET nombre=%s, documento=%s, telefono=%s, correo=%s,
                username=%s, password=%s, rol=%s
            WHERE id_usuarios=%s
        """, (nombre, documento, telefono, correo, username, password_hash, rol, id))

    # 🔥 SI NO → NO TOCAR PASSWORD
    else:
        cursor.execute("""
            UPDATE usuarios 
            SET nombre=%s, documento=%s, telefono=%s, correo=%s,
                username=%s, rol=%s
            WHERE id_usuarios=%s
        """, (nombre, documento, telefono, correo, username, rol, id))

    conexion.commit()
    conexion.close()


# 🗑️ ELIMINAR
def eliminar_usuario(id):
    delete_usuario(id)


# 📊 CONTAR (DASHBOARD)
def contar_usuarios():
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    total = cursor.fetchone()[0]
    conexion.close()
    return total