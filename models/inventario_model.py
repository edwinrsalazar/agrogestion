from database import get_db_connection

def obtener_productos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM INVENTARIO")
    data = cursor.fetchall()

    conn.close()
    return data