from flask import Blueprint, render_template, request, redirect, url_for
from services.usuario_service import (
    listar_usuarios, 
    registrar_usuario, 
    obtener_usuario, 
    editar_usuario, 
    eliminar_usuario
)
from utils.auth import login_required, admin_required

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

# LISTAR
@usuario_bp.route('/')
@login_required
def listar():
    usuarios = listar_usuarios()
    return render_template('usuarios/listar.html', usuarios=usuarios)

# CREAR (SOLO ADMIN)
@usuario_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        documento = request.form.get('documento')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        username = request.form.get('username')
        password = request.form.get('password')
        rol = request.form.get('rol')

        registrar_usuario(nombre, documento, telefono, correo, username, password, rol)

        return redirect(url_for('usuario.listar'))

    return render_template('usuarios/crear.html')

# EDITAR (SOLO ADMIN)
@usuario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    usuario = obtener_usuario(id)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        rol = request.form.get('rol')

        editar_usuario(id, username, password, rol)
        return redirect(url_for('usuario.listar'))

    return render_template('usuarios/editar.html', usuario=usuario)

# ELIMINAR (SOLO ADMIN)
@usuario_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    eliminar_usuario(id)
    return redirect(url_for('usuario.listar'))