from werkzeug.security import generate_password_hash
from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

password_hash = generate_password_hash("admin123")

cursor.execute("""
INSERT INTO usuarios (nombre, documento, telefono, correo, username, password, rol)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (
    'Admin',
    '0000',
    '0000',
    'admin@agro.com',
    'admin',
    password_hash,
    'admin'
))

conn.commit()
cursor.close()
conn.close()

print("Usuario admin creado correctamente")