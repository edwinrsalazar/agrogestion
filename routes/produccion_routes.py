from flask import Blueprint, render_template, request, redirect, url_for, session
from services.produccion_service import listar_produccion, crear_produccion
from services.cultivo_service import listar_cultivos

produccion_bp = Blueprint('produccion', __name__, url_prefix='/produccion')


# 🔒 LISTAR PRODUCCIÓN
@produccion_bp.route('/')
def listar():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    data = listar_produccion()
    return render_template('produccion/listar.html', produccion=data)


# ➕ CREAR PRODUCCIÓN
@produccion_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        cultivo_id = request.form.get('cultivo_id')
        cantidad = request.form.get('cantidad')
        fecha = request.form.get('fecha')

        if not cultivo_id or not cantidad or not fecha:
            return "Error: Todos los campos son obligatorios"

        crear_produccion(int(cultivo_id), float(cantidad), fecha)

        return redirect(url_for('produccion.listar'))

    cultivos = listar_cultivos()
    return render_template('produccion/crear.html', cultivos=cultivos)


# ✏️ EDITAR
@produccion_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    from services.produccion_service import obtener_produccion, actualizar_produccion

    if request.method == 'POST':
        cultivo_id = request.form.get('cultivo_id')
        cantidad = request.form.get('cantidad')
        fecha = request.form.get('fecha')

        if not cultivo_id or not cantidad or not fecha:
            return "Error: Todos los campos son obligatorios"

        actualizar_produccion(id, int(cultivo_id), float(cantidad), fecha)
        return redirect(url_for('produccion.listar'))

    produccion = obtener_produccion(id)
    cultivos = listar_cultivos()

    return render_template('produccion/editar.html', produccion=produccion, cultivos=cultivos)


# ❌ ELIMINAR (🔥 ESTA ES LA QUE TE FALTABA)
@produccion_bp.route('/eliminar/<int:id>')
def eliminar(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    from services.produccion_service import eliminar_produccion

    eliminar_produccion(id)

    return redirect(url_for('produccion.listar'))