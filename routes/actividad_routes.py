from flask import Blueprint, render_template, request, redirect, session
from services.actividad_service import listar_actividades, crear_actividad

actividad_bp = Blueprint('actividad', __name__)

@actividad_bp.route('/actividades')
def actividades():
    if 'usuario' not in session:
        return redirect('/')

    data = listar_actividades()
    return render_template('actividades/listar.html', actividades=data)


@actividad_bp.route('/crear_actividad', methods=['GET', 'POST'])
def crear_actividad_view():
    if 'usuario' not in session:
        return redirect('/')

    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        descripcion = request.form['descripcion']

        crear_actividad(nombre, fecha, descripcion)
        return redirect('/actividades')

    return render_template('actividades/crear.html')