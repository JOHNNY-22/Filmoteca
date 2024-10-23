from app.DB.database import Database

class Filmdb:

    @classmethod
    def get_connection(cls):
        return Database().get_connection()

    @classmethod
    def save_film(cls, pelicula):
        conn = cls.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(''' 
                INSERT INTO Films (Title, Director, Year, Rating, Duration, RecomendAge)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (pelicula.title, pelicula.director, pelicula.year, pelicula.rating, pelicula.duration, pelicula.recomend_age))

            pelicula_id = cursor.lastrowid
            conn.commit()
            return pelicula_id
        except Exception as e:
            print(f"Ocurrió un error al guardar la película: {e}")
            return None
        finally:
            conn.close()
