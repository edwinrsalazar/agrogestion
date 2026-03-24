from flask import Blueprint, render_template, request, redirect, session
from services.inventario_service import listar_inventario, crear_item

inventario_bp = Blueprint('inventario', __name__)

@inventario_bp.route('/inventario')
def inventario():
    if 'usuario' not in session:
        return redirect('/')

    data = listar_inventario()
    return render_template('inventario/listar.html', inventario=data)


@inventario_bp.route('/crear_item', methods=['GET', 'POST'])
def crear_item_view():
    if 'usuario' not in session:
        return redirect('/')

    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        unidad = request.form['unidad']

        crear_item(nombre, cantidad, unidad)
        return redirect('/inventario')

    return render_template('inventario/crear.html')