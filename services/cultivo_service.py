from models.cultivo_model import get_all_cultivos, create_cultivo, delete_cultivo, tiene_actividades
from models.cultivo_model import (get_all_cultivos, create_cultivo, get_cultivo_by_id, update_cultivo, delete_cultivo)

def listar_cultivos():
    return get_all_cultivos()


def crear_cultivo(nombre, tipo, ubicacion):
    if not nombre:
        return None

    create_cultivo(nombre, tipo, ubicacion)
    return True

def obtener_cultivo(id):
    return get_cultivo_by_id(id)


def actualizar_cultivo(id, nombre, tipo, ubicacion):
    if not nombre:
        return None
    update_cultivo(id, nombre, tipo, ubicacion)
    return True


def eliminar_cultivo(id):
    if tiene_actividades(id):
        return False  # No se puede eliminar

    delete_cultivo(id)
    return True

def contar_cultivos():
    from models.cultivo_model import get_db_connection
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM cultivos")
    total = cursor.fetchone()[0]
    conexion.close()
    return total