from flask import Blueprint, render_template, request, redirect, flash, session
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            flash("Login exitoso", "success")
            return redirect("/dashboard")
        else:
            flash("Credenciales incorrectas", "danger")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form["nombre"]
        documento = request.form["documento"]
        correo = request.form["correo"]
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        rol = request.form["rol"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nombre, documento, correo, username, password, rol)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, documento, correo, username, password, rol))

        conn.commit()
        cursor.close()
        conn.close()

        flash("Usuario registrado correctamente", "success")
        return redirect("/")

    return render_template("register.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")