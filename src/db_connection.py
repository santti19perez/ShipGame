# Archivo: src/db_connection.py

import sys
sys.path.append("src")

import psycopg2
from config import PGHOST, PGDATABASE, PGUSER, PGPASSWORD, PGPORT

def get_connection():
    try:
        connection = psycopg2.connect(
            host=PGHOST,
            database=PGDATABASE,
            user=PGUSER,
            password=PGPASSWORD,
            port=PGPORT
        )
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
