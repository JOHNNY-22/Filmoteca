from DB.database import Database


def crear_tablas():
    conn = Database().get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Films(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Director TEXT NOT NULL,
            Year INTEGER NOT NULL,
            Rating INTEGER NOT NULL,
            Duration INTEGER NOT NULL, 
            RecomendAge INTEGER NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Gendres (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL UNIQUE
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS peliculas_generos (
            Film_id INTEGER,
            Gendre_id INTEGER,
            FOREIGN KEY (Film_id) REFERENCES Films (Id),
            FOREIGN KEY (Gendre_id) REFERENCES Gendres (Id),
            PRIMARY KEY (Film_id, Gendre_id)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Actors (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Surname TEXT, 
            Gendre TEXT,
            Year INTEGER
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACTORS_FILMS(
            Film_Id INTEGER,
            Actor_Id INTEGER,
            FOREIGN KEY (Film_Id) REFERENCES Films (Id),
            FOREIGN KEY (Actor_Id) REFERENCES Actors (Id),
            PRIMARY KEY (Film_Id, Actor_Id)
        )
        ''')
        conn.commit()
    except Exception as e:
        print(f"Ocurrió un error al crear las tablas: {e}")
    finally:
        cursor.close()
