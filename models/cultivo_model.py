from database import get_db_connection


def get_all_cultivos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM CULTIVOS")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def create_cultivo(nombre, tipo, tiempo_cosecha_dias):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO CULTIVOS (nombre, tipo, tiempo_cosecha_dias) VALUES (%s, %s, %s)",
        (nombre, tipo, tiempo_cosecha_dias)
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_cultivo_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM CULTIVOS WHERE id_cultivos=%s", (id,))
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


def update_cultivo(id, nombre, tipo, tiempo_cosecha_dias):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE CULTIVOS 
        SET nombre=%s, tipo=%s, tiempo_cosecha_dias=%s
        WHERE id_cultivos=%s
    """, (nombre, tipo, tiempo_cosecha_dias, id))

    conn.commit()
    cursor.close()
    conn.close()


def delete_cultivo(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM CULTIVOS WHERE id_cultivos=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()