from database import get_db_connection

def get_all_produccion():
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            p.id,
            p.cantidad,
            p.fecha,
            c.nombre AS cultivo
        FROM produccion p
        INNER JOIN cultivos c ON p.id_cultivo = c.id_cultivos
    """)

    data = cursor.fetchall()
    conexion.close()

    return data


def create_produccion(id_cultivo, cantidad, fecha):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO produccion (id_cultivo, cantidad, fecha) VALUES (%s, %s, %s)",
        (id_cultivo, cantidad, fecha)
    )

    conn.commit()
    cursor.close()
    conn.close()