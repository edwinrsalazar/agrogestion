from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",  # pon tu contraseña si tienes
        database="agrogestion2"
    )

@app.route("/")
def home():
    return "Servidor funcionando 🚀"

@app.route("/crear_usuario")
def crear_usuario():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO usuario (nombre, documento, correo, username, password, rol)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            "Edwin Salazar",
            "123456789",
            "edwin@email.com",
            "edwin",
            "1234",
            "admin"
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return "Usuario creado correctamente ✅"

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)