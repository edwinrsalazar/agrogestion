import mysql.connector
from config import Config

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database="agrogestion"
    )