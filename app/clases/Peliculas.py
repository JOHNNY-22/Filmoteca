class Pelicula:
    def __init__(self, title, director, year, gendres, actors, rating, duration, recomend_age):
        self.title = title
        self.director = director
        self.year = year
        self.gendres = gendres
        self.actors = actors
        self.rating = rating
        self.duration = duration
        self.recomend_age = recomend_age

    def __str__(self):
        generos_str = ", ".join(self.gendres)
        actores_str = ", ".join(self.actors)
        return (f"Pelicula: {self.title} ({self.year})\n"
                f"Director: {self.director}\n"
                f"Géneros: {generos_str}\n"
                f"Actores: {actores_str}\n"
                f"Clasificación: {self.rating}\n"
                f"Duración: {self.duration} minutos")

    def eslarga(self): 
        return self.duration > 120
    
    def es_apta_para_ninos(self):
        return self.recomend_age <= 18

    def save_film(self):
        from app.DB.Models.Films import Filmdb 
        if all([self.title, self.director, self.year, self.gendres]):
            return Filmdb.save_film(self)
        return False
