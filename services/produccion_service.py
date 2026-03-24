from models.produccion_model import get_all_produccion, create_produccion

def listar_produccion():
    return get_all_produccion()


def crear_produccion(cultivo_id, cantidad, fecha):
    if cantidad <= 0:
        return None

    create_produccion(cultivo_id, cantidad, fecha)
    return True