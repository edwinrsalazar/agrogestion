from flask import Flask, session, redirect, url_for, render_template
from config import Config
from database import get_db_connection

# IMPORTAR BLUEPRINTS
from routes.auth_routes import auth_bp
from routes.usuario_routes import usuario_bp
from routes.cultivo_routes import cultivo_bp
from routes.inventario_routes import inventario_bp
from routes.actividades_routes import actividad_bp

# IMPORTAR MODELOS (IMPORTANTE 🔥)
from models.inventario_model import get_total_productos, get_total_cantidad

from functools import wraps

app = Flask(__name__)

# CONFIGURACIÓN
app.config.from_object(Config)

# REGISTRAR BLUEPRINTS
app.register_blueprint(auth_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(cultivo_bp)
app.register_blueprint(inventario_bp)
app.register_blueprint(actividad_bp)


# 🔐 DECORADOR GLOBAL
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


# 📊 DASHBOARD PROTEGIDO
@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # 📊 CULTIVOS
    cursor.execute("SELECT COUNT(*) as total FROM cultivos")
    cultivos = cursor.fetchone()['total']

    # 👤 USUARIOS
    cursor.execute("SELECT COUNT(*) as total FROM usuarios")
    usuarios = cursor.fetchone()['total']

    # 🌾 PRODUCCIÓN
    cursor.execute("SELECT COUNT(*) as total FROM produccion")
    produccion = cursor.fetchone()['total']

    cursor.close()
    conn.close()

    # 📦 INVENTARIO (desde modelo 🔥)
    total_productos = get_total_productos()
    total_cantidad = get_total_cantidad()

    print("TOTAL INVENTARIO:", total_cantidad)  # DEBUG

    return render_template(
        'dashboard.html',
        cultivos=cultivos,
        usuarios=usuarios,
        produccion=produccion,
        total_productos=total_productos,
        total_cantidad=total_cantidad
    )


# 🚀 EJECUTAR APP
if __name__ == '__main__':
    app.run(debug=True)