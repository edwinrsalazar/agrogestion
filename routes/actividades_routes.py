from flask import Blueprint, render_template, request, redirect, url_for
from models.actividades_model import *
from models.cultivo_model import get_all_cultivos

actividad_bp = Blueprint('actividades', __name__, url_prefix='/actividades')


# LISTAR
@actividad_bp.route('/')
def listar():
    actividades = get_all_actividades()
    return render_template('actividades/listar.html', actividades=actividades)


# CREAR
@actividad_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    cultivos = get_all_cultivos()

    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        id_cultivo = request.form.get('id_cultivo')

        # 🔥 VALIDACIÓN CLAVE
        if not id_cultivo:
            return "⚠️ Debes seleccionar un cultivo"

        id_cultivo = int(id_cultivo)

        create_actividad(descripcion, fecha, id_cultivo)

        return redirect(url_for('actividades.listar'))

    return render_template('actividades/crear.html', cultivos=cultivos)

#EDITAR
@actividad_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        id_cultivo = request.form['id_cultivo']

        # 🔥 VALIDACIÓN
        if not id_cultivo:
            return "⚠️ Debes seleccionar un cultivo"

        id_cultivo = int(id_cultivo)

        cursor.execute("""
            UPDATE actividades
            SET descripcion=%s, fecha=%s, id_cultivo=%s
            WHERE id=%s
        """, (descripcion, fecha, id_cultivo, id))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('actividades.listar'))

    cursor.execute("SELECT * FROM actividades WHERE id=%s", (id,))
    actividad = cursor.fetchone()

    cursor.close()
    conn.close()

    cultivos = get_all_cultivos()

    return render_template(
        'actividades/editar.html',
        actividad=actividad,
        cultivos=cultivos
    )


# ELIMINAR
@actividad_bp.route('/eliminar/<int:id>')
def eliminar(id):
    delete_actividad(id)
    return redirect(url_for('actividades.listar'))