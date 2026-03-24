from flask import Blueprint, render_template, request, redirect, url_for, session
from services.usuario_service import validar_usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return render_template('login.html', error="Faltan datos")

        user = validar_usuario(username, password)

        if user:
            session['user_id'] = user['id_usuarios']
            session['username'] = user['username']
            session['rol'] = user['rol']   # 🔥 ESTA ES LA CLAVE

            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Credenciales incorrectas")

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')