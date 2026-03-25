from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

from services.cultivo_service import (
    listar_cultivos, crear_cultivo,
    obtener_cultivo, actualizar_cultivo, eliminar_cultivo
)

# Blueprint con prefijo correcto
cultivo_bp = Blueprint('cultivo', __name__, url_prefix='/cultivos')


# 🔐 Decorador reutilizable
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


# 📋 LISTAR
@cultivo_bp.route('/')
@login_required
def listar():
    data = listar_cultivos()
    return render_template('cultivos/listar.html', cultivos=data)


# ➕ CREAR
@cultivo_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    if request.method == 'POST':
        crear_cultivo(
            request.form['nombre'],
            request.form['tipo'],
            request.form['tiempo_cosecha_dias']
        )
        return redirect(url_for('cultivo.listar'))

    return render_template('cultivos/crear.html')


# ✏️ EDITAR
@cultivo_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    cultivo = obtener_cultivo(id)

    if request.method == 'POST':
        actualizar_cultivo(
            id,
            request.form['nombre'],
            request.form['tipo'],
            request.form['tiempo_cosecha_dias']
        )
        return redirect(url_for('cultivo.listar'))

    return render_template('cultivos/editar.html', cultivo=cultivo)


# ❌ ELIMINAR
@cultivo_bp.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    eliminar_cultivo(id)
    return redirect(url_for('cultivo.listar'))