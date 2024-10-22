import tkinter as tk
from tkinter import messagebox
from database import crear_tabla, guardar_pelicula as guardar_pelicula_db

crear_tabla()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Películas")

# Definir las etiquetas y campos de entrada
label_titulo = tk.Label(root, text="Título de la película:")
label_titulo.grid(row=0, column=0, padx=10, pady=10)
entry_titulo = tk.Entry(root)
entry_titulo.grid(row=0, column=1, padx=10, pady=10)

label_director = tk.Label(root, text="Director:")
label_director.grid(row=1, column=0, padx=10, pady=10)
entry_director = tk.Entry(root)
entry_director.grid(row=1, column=1, padx=10, pady=10)

label_anio = tk.Label(root, text="Año de lanzamiento:")
label_anio.grid(row=2, column=0, padx=10, pady=10)
entry_anio = tk.Entry(root)
entry_anio.grid(row=2, column=1, padx=10, pady=10)

label_genero = tk.Label(root, text="Género:")
label_genero.grid(row=3, column=0, padx=10, pady=10)
entry_genero = tk.Entry(root)
entry_genero.grid(row=3, column=1, padx=10, pady=10)

def guardar_pelicula():
    titulo = entry_titulo.get()
    director = entry_director.get()
    anio = entry_anio.get()
    genero = entry_genero.get()

    if titulo and director and anio and genero:
        guardar_pelicula_db(titulo, director, anio, genero)  # Guardar en la base de datos
        messagebox.showinfo("Éxito", f"Película '{titulo}' guardada correctamente.")
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")


# Botón para guardar la película
boton_guardar = tk.Button(root, text="Guardar", command=guardar_pelicula)
boton_guardar.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar el loop principal de la interfaz
root.mainloop()
