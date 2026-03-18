from database import get_db_connection

def obtener_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    data = cursor.fetchall()

    conn.close()
    return data