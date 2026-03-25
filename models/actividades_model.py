from database import get_db_connection


# LISTAR
def get_all_actividades():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT a.*, c.nombre AS cultivo
        FROM actividades a
        LEFT JOIN cultivos c ON a.id_cultivo = c.id_cultivos
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


# CREAR
def create_actividad(descripcion, fecha, id_cultivo):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO actividades (descripcion, fecha, id_cultivo)
        VALUES (%s, %s, %s)
    """, (descripcion, fecha, id_cultivo))

    conn.commit()
    cursor.close()
    conn.close()


# ELIMINAR
def delete_actividad(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM actividades WHERE id = %s", (id,))

    conn.commit()
    cursor.close()
    conn.close()