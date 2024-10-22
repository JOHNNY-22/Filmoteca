from database import guardar_pelicula, guardar_genero, asociar_pelicula_genero, crear_tablas

class Pelicula:
    def __init__(self, titulo, director, anio, generos):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.generos = generos  # Lista de géneros

    def guardar(self):
        if all([self.titulo, self.director, self.anio, self.generos]):
            guardar_pelicula(self.titulo, self.directorbv, self.anio)
            pelicula_id = self.obtener_id_pelicula()
            for genero in self.generos:
                guardar_genero(genero)
                genero_id = self.obtener_id_genero(genero)
                asociar_pelicula_genero(pelicula_id, genero_id)
            return True
        return False

    def obtener_id_pelicula(self):
        # Método para obtener el ID de la película recién insertada
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM peliculas WHERE titulo = ? AND director = ? AND anio = ?',
                       (self.titulo, self.director, self.anio))
        pelicula_id = cursor.fetchone()[0]
        conn.close()
        return pelicula_id

    def obtener_id_genero(self, nombre):
        # Método para obtener el ID del género
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM generos WHERE nombre = ?', (nombre,))
        genero_id = cursor.fetchone()[0]
        conn.close()
        return genero_id

    @staticmethod
    def inicializar_db():
        crear_tablas()
