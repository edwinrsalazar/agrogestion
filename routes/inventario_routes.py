from flask import Blueprint, render_template, request, redirect, url_for
from database import get_db_connection

inventario_bp = Blueprint('inventario', __name__, url_prefix='/inventario')

# LISTAR
@inventario_bp.route('/')
def listar():
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM inventario")
    inventarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template('inventario/listar.html', inventarios=inventarios)


# CREAR
@inventario_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        unidad = request.form['unidad']
        precio = request.form['precio']

        conexion = get_db_connection()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO inventario (nombre, cantidad, unidad, precio)
            VALUES (%s, %s, %s, %s)
        """, (nombre, cantidad, unidad, precio))

        conexion.commit()
        cursor.close()
        conexion.close()

        return redirect(url_for('inventario.listar'))

    return render_template('inventario/crear.html')


# EDITAR
@inventario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        cursor.execute("""
            UPDATE inventario
            SET nombre=%s, cantidad=%s, precio=%s
            WHERE id=%s
        """, (nombre, cantidad, precio, id))

        conexion.commit()
        cursor.close()
        conexion.close()

        return redirect(url_for('inventario.listar'))

    cursor.execute("SELECT * FROM inventario WHERE id=%s", (id,))
    inventario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template('inventario/editar.html', inventario=inventario)


# ELIMINAR
@inventario_bp.route('/eliminar/<int:id>')
def eliminar(id):
    conexion = get_db_connection()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM inventario WHERE id=%s", (id,))
    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect(url_for('inventario.listar'))