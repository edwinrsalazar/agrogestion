from models.actividades_model import get_all_actividades, create_actividad, get_db_connection

def listar_actividades():
    return get_all_actividades()

def crear_actividad(descripcion, fecha, id_cultivo):
    if not descripcion or not fecha or not id_cultivo:
        return None

    create_actividad(descripcion, fecha, id_cultivo)
    return True

def contar_actividades():
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM actividades")
    total = cursor.fetchone()[0]
    conexion.close()
    return total