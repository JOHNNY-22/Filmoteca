import sqlite3
import os

# Ruta donde se guardará la base de datos
db_path = os.path.join(os.path.dirname(__file__), '../data/peliculas.db')

# Conectar a la base de datos (si no existe, se creará automáticamente)
def conectar():
    conn = sqlite3.connect(db_path)
    return conn

# Crear las tablas de películas y géneros
def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()
    
    # Crear tabla de películas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS peliculas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Director TEXT NOT NULL,
        Year INTEGER NOT NULL
    )
    ''')
    
    # Crear tabla de géneros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS generos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL UNIQUE
    )
    ''')
    
    # Crear tabla intermedia de relación entre películas y géneros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS peliculas_generos (
        film_id INTEGER,
        gendre_id INTEGER,
        FOREIGN KEY (film_id) REFERENCES peliculas (id),
        FOREIGN KEY (gendre_id) REFERENCES generos (id),
        PRIMARY KEY (film_id, gendre_id)
    )
    ''')
    
    conn.commit()
    conn.close()

# Guardar película en la base de datos
def guardar_pelicula(titulo, director, anio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO peliculas (Title, Director , Year)
    VALUES (?, ?, ?)
    ''', (titulo, director, anio))
    conn.commit()
    conn.close()

# Guardar género en la base de datos
def guardar_genero(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR IGNORE INTO generos (nombre)
    VALUES (?)
    ''', (nombre,))
    conn.commit()
    conn.close()

# Asociar película con género en la tabla intermedia
def asociar_pelicula_genero(pelicula_id, genero_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO peliculas_generos (pelicula_id, genero_id)
    VALUES (?, ?)
    ''', (pelicula_id, genero_id))
    conn.commit()
    conn.close()

# Crear las tablas al iniciar
def inicializar_db():
    crear_tablas()
