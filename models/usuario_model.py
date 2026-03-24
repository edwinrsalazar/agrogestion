from database import get_db_connection

def get_usuario_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def get_all_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return usuarios


def create_usuario(nombre, documento, telefono, correo, username, password, rol):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios 
        (nombre, documento, telefono, correo, username, password, rol) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nombre, documento, telefono, correo, username, password, rol))

    conn.commit()
    cursor.close()
    conn.close()

def get_usuario_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE id_usuarios = %s", (id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def update_usuario(id, username, password, rol):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE usuarios 
        SET username = %s, password = %s, rol = %s
        WHERE id_usuarios = %s
    """, (username, password, rol, id))

    conn.commit()
    cursor.close()
    conn.close()

def delete_usuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id_usuarios = %s", (id,))

    conn.commit()
    cursor.close()
    conn.close()