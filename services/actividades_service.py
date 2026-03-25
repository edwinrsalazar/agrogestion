from models.actividades_model import get_all_actividades, create_actividad

def listar_actividades():
    return get_all_actividades()


def crear_actividad(nombre, fecha, descripcion):
    if not nombre or not fecha:
        return None

    create_actividad(nombre, fecha, descripcion)
    return True