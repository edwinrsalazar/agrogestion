from models.inventario_model import get_all_inventario, create_item, get_db_connection

def listar_inventario():
    return get_all_inventario()


def crear_item(nombre, cantidad, unidad):
    if not nombre or cantidad <= 0:
        return None

    create_item(nombre, cantidad, unidad)
    return True

def contar_inventario():
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT SUM(cantidad) FROM inventario")
    total = cursor.fetchone()[0] or 0
    conexion.close()
    return total


def contar_productos():
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM inventario")
    total = cursor.fetchone()[0]
    conexion.close()
    return total