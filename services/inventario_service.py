from models.inventario_model import get_all_inventario, create_item

def listar_inventario():
    return get_all_inventario()


def crear_item(nombre, cantidad, unidad):
    if not nombre or cantidad <= 0:
        return None

    create_item(nombre, cantidad, unidad)
    return True