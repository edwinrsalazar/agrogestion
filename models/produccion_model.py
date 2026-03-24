from database import get_db_connection

def get_all_produccion():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM produccion")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def create_produccion(cultivo_id, cantidad, fecha):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO produccion (cultivo_id, cantidad, fecha) VALUES (%s, %s, %s)",
        (cultivo_id, cantidad, fecha)
    )

    conn.commit()
    cursor.close()
    conn.close()