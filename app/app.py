import tkinter as tk
from tkinter import messagebox
from clases.Peliculas import Pelicula
from DB.tables import crear_tablas

crear_tablas()

root = tk.Tk()
root.title("Gestor de Películas")

label_Title = tk.Label(root, text="Título de la película:")
label_Title.grid(row=0, column=0, padx=10, pady=10)
entry_Title = tk.Entry(root)
entry_Title.grid(row=0, column=1, padx=10, pady=10)

label_Director = tk.Label(root, text="Director:")
label_Director.grid(row=1, column=0, padx=10, pady=10)
entry_Director = tk.Entry(root)
entry_Director.grid(row=1, column=1, padx=10, pady=10)

label_Anyo = tk.Label(root, text="Year:")
label_Anyo.grid(row=2, column=0, padx=10, pady=10)
entry_Anyo = tk.Entry(root)
entry_Anyo.grid(row=2, column=1, padx=10, pady=10)

label_Gendres = tk.Label(root, text="Géneros:")
label_Gendres.grid(row=3, column=0, padx=10, pady=10)
entry_Gendres = tk.Entry(root)
entry_Gendres.grid(row=3, column=1, padx=10, pady=10)

label_Actors = tk.Label(root, text="Actores:")
label_Actors.grid(row=4, column=0, padx=10, pady=10)
entry_Actors = tk.Entry(root)
entry_Actors.grid(row=4, column=1, padx=10, pady=10)

label_Rating = tk.Label(root, text="Rating:")
label_Rating.grid(row=5, column=0, padx=10, pady=10)
entry_Rating = tk.Entry(root)
entry_Rating.grid(row=5, column=1, padx=10, pady=10)

label_Duration = tk.Label(root, text="Duración (minutos):")
label_Duration.grid(row=6, column=0, padx=10, pady=10)
entry_Duration = tk.Entry(root)
entry_Duration.grid(row=6, column=1, padx=10, pady=10)

label_RecomendAge = tk.Label(root, text="Edad recomendada:")
label_RecomendAge.grid(row=7, column=0, padx=10, pady=10)
entry_RecomendAge = tk.Entry(root)
entry_RecomendAge.grid(row=7, column=1, padx=10, pady=10)

def guardar_pelicula():
    nueva_pelicula = Pelicula(
        entry_Title.get(),
        entry_Director.get(),
        entry_Anyo.get(),
        entry_Gendres.get(),
        entry_Actors.get(),
        entry_Rating.get(),
        entry_Duration.get(),
        entry_RecomendAge.get()
    )
    pelicula_id = nueva_pelicula.save_film()  # Guarda la película en la BD
    if pelicula_id:
        messagebox.showinfo("Éxito", f"Película guardada con ID: {pelicula_id}")
    else:
        messagebox.showerror("Error", "No se pudo guardar la película.")

boton_guardar = tk.Button(root, text="Guardar", command=guardar_pelicula)
boton_guardar.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
