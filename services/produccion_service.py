from models.produccion_model import (
    get_all_produccion,
    create_produccion,
    get_db_connection
)


# 📋 LISTAR
def listar_produccion():
    return get_all_produccion()


# ➕ CREAR
def crear_produccion(id_cultivo, cantidad, fecha):
    if cantidad <= 0:
        return None

    create_produccion(id_cultivo, cantidad, fecha)
    return True


# 🔍 OBTENER POR ID
def obtener_produccion(id):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM produccion WHERE id = %s", (id,))
    data = cursor.fetchone()

    conexion.close()
    return data


# ✏️ ACTUALIZAR
def actualizar_produccion(id, id_cultivo, cantidad, fecha):
    conexion = get_db_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE produccion 
        SET id_cultivo = %s, cantidad = %s, fecha = %s
        WHERE id = %s
    """, (id_cultivo, cantidad, fecha, id))

    conexion.commit()
    conexion.close()


# ❌ ELIMINAR
def eliminar_produccion(id):
    conexion = get_db_connection()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM produccion WHERE id = %s", (id,))

    conexion.commit()
    conexion.close()


# 📊 CONTAR (DASHBOARD)
def contar_produccion():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM produccion")
    total = cursor.fetchone()[0]

    conexion.close()
    return total