from flask import Flask, session, redirect, url_for, render_template
from config import Config

# IMPORTAR TODAS LAS RUTAS
from routes.auth_routes import auth_bp
from routes.usuario_routes import usuario_bp
from routes.cultivo_routes import cultivo_bp
from routes.inventario_routes import inventario_bp
from routes.actividad_routes import actividad_bp

app = Flask(__name__)

# CONFIGURACIÓN
app.config.from_object(Config)

# 🔐 CLAVE DE SESIÓN (OBLIGATORIO)
app.secret_key = "clave_super_segura_123"

# REGISTRAR BLUEPRINTS
app.register_blueprint(auth_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(cultivo_bp)
app.register_blueprint(inventario_bp)
app.register_blueprint(actividad_bp)

# DASHBOARD (PROTEGIDO)
@app.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))

    return render_template('dashboard.html')

# EJECUTAR APP
if __name__ == '__main__':
    app.run(debug=True)