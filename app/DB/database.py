import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), '../data/peliculas.db')

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            db_dir = os.path.dirname(db_path)
            os.makedirs(db_dir, exist_ok=True)  # Crea la carpeta de datos si no existe
            cls._instance.connection = sqlite3.connect(db_path)
            cls._instance.connection.row_factory = sqlite3.Row
            cls._instance.connection.row_factory = sqlite3.Row
        return cls._instance

    def get_connection(self):
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            Database._instance = None
