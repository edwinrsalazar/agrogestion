from flask import Blueprint, render_template, request, redirect, url_for, session
from services.usuario_service import validar_usuario

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    # Si ya está logueado → lo mandamos al dashboard
    if session.get('user_id'):
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validación básica
        if not username or not password:
            return render_template('login.html', error="Faltan datos")

        # Validar usuario en BD
        user = validar_usuario(username, password)

        if user:
            # 🔐 GUARDAR SESIÓN (CLAVE DEL SISTEMA)
            session['user_id'] = user['id_usuarios']
            session['username'] = user['username']
            session['rol'] = user['rol']

            return redirect(url_for('dashboard'))

        else:
            return render_template('login.html', error="Credenciales incorrectas")

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))