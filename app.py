from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "super_clave_secreta_123"


# 🔹 Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",  # cambia si tu contraseña es diferente
        database="agrogestion"
    )


# 🔹 Home
@app.route("/")
def home():
    return redirect("/login")


# 🔹 Registro de usuarios (solo admin)
@app.route("/register", methods=["GET", "POST"])
def register():

    if "usuario" not in session or session.get("rol") != "admin":
        flash("No tienes permiso para acceder aquí", "danger")
        return redirect("/dashboard")

    if request.method == "POST":

        nombre = request.form["nombre"]
        documento = request.form["documento"]
        correo = request.form["correo"]
        username = request.form["username"]
        password = request.form["password"]
        rol = request.form["rol"]

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO usuarios (nombre, documento, correo, username, password, rol)
            VALUES (%s,%s,%s,%s,%s,%s)
            """

            valores = (nombre, documento, correo, username, password, rol)

            cursor.execute(sql, valores)
            conn.commit()

            cursor.close()
            conn.close()

            flash("Usuario creado correctamente", "success")
            return redirect("/dashboard")

        except Exception as e:
            flash(f"Error: {e}", "danger")

    return render_template("register.html")


# 🔹 Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuarios WHERE username=%s AND password=%s",
            (username, password)
        )

        usuario = cursor.fetchone()

        cursor.close()
        conn.close()

        if usuario:
            session["usuario"] = usuario["nombre"]
            session["rol"] = usuario["rol"]

            return redirect("/dashboard")

        else:
            flash("Usuario o contraseña incorrectos", "danger")

    return render_template("login.html")


# 🔹 Dashboard
@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect("/login")

    return render_template("dashboard.html")

@app.route("/usuarios")
def usuarios():

    if "usuario" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    lista_usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("usuarios.html", usuarios=lista_usuarios)


# 🔹 Cerrar sesión
@app.route("/logout")
def logout():

    session.clear()
    flash("Sesión cerrada correctamente", "info")

    return redirect("/login")

@app.route("/editar_usuario/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):

    if "usuario" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":

        nombre = request.form["nombre"]
        documento = request.form["documento"]
        correo = request.form["correo"]
        username = request.form["username"]
        rol = request.form["rol"]

        sql = """
        UPDATE usuarios
        SET nombre=%s, documento=%s, correo=%s, username=%s, rol=%s
        WHERE id_usuario=%s
        """

        valores = (nombre, documento, correo, username, rol, id)

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        flash("Usuario actualizado correctamente", "success")

        return redirect("/usuarios")

    cursor.execute("SELECT * FROM usuarios WHERE id_usuario=%s", (id,))
    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/eliminar_usuario/<int:id>")
def eliminar_usuario(id):

    if "usuario" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id_usuario=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    flash("Usuario eliminado correctamente", "info")

    return redirect("/usuarios")


if __name__ == "__main__":
    app.run(debug=True)

