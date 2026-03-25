from database import get_db_connection


# 📦 OBTENER TODOS LOS REGISTROS
def get_all_inventario():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM inventario")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


# 🔍 OBTENER UN ITEM POR ID
def get_item_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM inventario WHERE id = %s", (id,))
    item = cursor.fetchone()

    cursor.close()
    conn.close()

    return item


# ➕ CREAR ITEM
def create_item(nombre, cantidad, unidad, precio):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inventario (nombre, cantidad, unidad, precio)
        VALUES (%s, %s, %s, %s)
    """, (nombre, cantidad, unidad, precio))

    conn.commit()

    cursor.close()
    conn.close()


# ✏️ ACTUALIZAR ITEM
def update_item(id, nombre, cantidad, unidad, precio):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE inventario
        SET nombre = %s, cantidad = %s, unidad = %s, precio = %s
        WHERE id = %s
    """, (nombre, cantidad, unidad, precio, id))

    conn.commit()

    cursor.close()
    conn.close()


# 🗑️ ELIMINAR ITEM
def delete_item(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM inventario WHERE id = %s", (id,))

    conn.commit()

    cursor.close()
    conn.close()


# 📊 TOTAL PRODUCTOS (COUNT)
def get_total_productos():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM inventario")
    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total if total else 0


# 📊 SUMA TOTAL INVENTARIO (SUM)
def get_total_cantidad():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(cantidad) FROM inventario")
    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total if total else 0