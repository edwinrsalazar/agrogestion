from flask import Blueprint, render_template, request, redirect, url_for, session
from services.usuario_service import validar_usuario, contar_usuarios
from services.cultivo_service import contar_cultivos
from services.inventario_service import contar_inventario, contar_productos
from services.actividades_service import contar_actividades
from utils.auth import login_required

auth_bp = Blueprint('auth', __name__)


# LOGIN
@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if session.get('user_id'):
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return render_template('login.html', error="Faltan datos")

        user = validar_usuario(username, password)

        if user:
            session['user_id'] = user['id_usuarios']
            session['username'] = user['username']
            session['rol'] = user['rol']

            return redirect(url_for('auth.dashboard'))
        else:
            return render_template('login.html', error="Credenciales incorrectas")

    return render_template('login.html')


# LOGOUT
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


# DASHBOARD
@auth_bp.route('/dashboard')
@login_required
def dashboard():

    rol = session.get('rol')

    # 🔥 DATOS DEL DASHBOARD
    total_usuarios = contar_usuarios()
    total_cultivos = contar_cultivos()
    total_cantidad = contar_inventario()
    total_productos = contar_productos()
    total_actividades = contar_actividades()

    # 👨‍💼 ADMIN
    if rol == 'admin':
        return render_template(
            'dashboard_admin.html',
            usuarios=total_usuarios,
            cultivos=total_cultivos,
            total_cantidad=total_cantidad,
            total_productos=total_productos,
            actividades=total_actividades
        )

    # 👨‍🌾 USUARIO (AHORA CON DATOS 🔥)
    else:
        return render_template(
            'dashboard_usuario.html',
            cultivos=total_cultivos,
            actividades=total_actividades
        )