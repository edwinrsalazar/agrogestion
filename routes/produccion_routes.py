from flask import Blueprint, render_template, request, redirect, session
from services.produccion_service import listar_produccion, crear_produccion

produccion_bp = Blueprint('produccion', __name__)

@produccion_bp.route('/produccion')
def produccion():
    if 'usuario' not in session:
        return redirect('/')

    data = listar_produccion()
    return render_template('produccion/listar.html', produccion=data)


@produccion_bp.route('/crear_produccion', methods=['GET', 'POST'])
def crear_produccion_view():
    if 'usuario' not in session:
        return redirect('/')

    if request.method == 'POST':
        cultivo_id = int(request.form['cultivo_id'])
        cantidad = float(request.form['cantidad'])
        fecha = request.form['fecha']

        crear_produccion(cultivo_id, cantidad, fecha)
        return redirect('/produccion')

    return render_template('produccion/crear.html')