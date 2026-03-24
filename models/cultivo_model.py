from database import get_db_connection

def get_all_cultivos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cultivos")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def create_cultivo(nombre, tipo, ubicacion):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cultivos (nombre, tipo, ubicacion) VALUES (%s, %s, %s)",
        (nombre, tipo, ubicacion)
    )

    conn.commit()
    cursor.close()
    conn.close()

def get_cultivo_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cultivos WHERE id=%s", (id,))
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


def update_cultivo(id, nombre, tipo, ubicacion):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE cultivos 
        SET nombre=%s, tipo=%s, ubicacion=%s 
        WHERE id=%s
    """, (nombre, tipo, ubicacion, id))

    conn.commit()
    cursor.close()
    conn.close()


def delete_cultivo(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cultivos WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()