from flask import Blueprint, render_template, request, redirect, url_for, session
from services.produccion_service import listar_produccion, crear_produccion

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
        cultivo_id = int(request.form['cultivo_id'])
        cantidad = float(request.form['cantidad'])
        fecha = request.form['fecha']

        crear_produccion(cultivo_id, cantidad, fecha)
        return redirect(url_for('produccion.listar'))

    return render_template('produccion/crear.html')