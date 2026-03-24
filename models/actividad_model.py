from database import get_db_connection

def get_all_actividades():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM actividades")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def create_actividad(nombre, fecha, descripcion):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO actividades (nombre, fecha, descripcion) VALUES (%s, %s, %s)",
        (nombre, fecha, descripcion)
    )

    conn.commit()
    cursor.close()
    conn.close()