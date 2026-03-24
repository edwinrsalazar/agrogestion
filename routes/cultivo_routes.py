from flask import Blueprint, render_template, request, redirect, session
from services.cultivo_service import (
    listar_cultivos, crear_cultivo,
    obtener_cultivo, actualizar_cultivo, eliminar_cultivo
)

cultivo_bp = Blueprint('cultivo', __name__)

@cultivo_bp.route('/cultivos')
def cultivos():
    if 'usuario' not in session:
        return redirect('/')

    data = listar_cultivos()
    return render_template('cultivos/listar.html', cultivos=data)


@cultivo_bp.route('/cultivos/crear', methods=['GET', 'POST'])
def crear_cultivo_view():
    if 'usuario' not in session:
        return redirect('/')

    if request.method == 'POST':
        crear_cultivo(
            request.form['nombre'],
            request.form['tipo'],
            request.form['ubicacion']
        )
        return redirect('/cultivos')

    return render_template('cultivos/crear.html')


@cultivo_bp.route('/cultivos/editar/<int:id>', methods=['GET', 'POST'])
def editar_cultivo(id):
    if 'usuario' not in session:
        return redirect('/')

    cultivo = obtener_cultivo(id)

    if request.method == 'POST':
        actualizar_cultivo(
            id,
            request.form['nombre'],
            request.form['tipo'],
            request.form['ubicacion']
        )
        return redirect('/cultivos')

    return render_template('cultivos/editar.html', cultivo=cultivo)


@cultivo_bp.route('/cultivos/eliminar/<int:id>')
def eliminar_cultivo_view(id):
    if 'usuario' not in session:
        return redirect('/')

    eliminar_cultivo(id)
    return redirect('/cultivos')