import tkinter as tk
from tkinter import PhotoImage
from dashboard import show_dashboard
from data_view import show_data
from map_view import show_map 
from algorithms import show_algorithms
from utils import clear_frame, logout
from login import login_window

class Menu:
    def __init__(self, parent):
        self.parent = parent
        
        # Crear una barra lateral en el grid (columna 0)
        self.sidebar_frame = tk.Frame(self.parent, bg="#5F95FF", width=220)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")
        
        # Crear el frame principal para el contenido en la columna 1
        self.main_frame = tk.Frame(self.parent, bg="white")
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        
        # Asegurar que la columna 1 (el contenido) se expanda con la ventana
        self.parent.grid_columnconfigure(1, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)
        
        # Cargar imágenes para cada botón
        self.button_images = {
            "dashboard": PhotoImage(file="assets/ButtonDash.png"),  # Imagen para el botón Dashboard
            "maps": PhotoImage(file="assets/ButtonMap.png"),             # Imagen para el botón Mapa
            "datos": PhotoImage(file="assets/ButtonData.png"),           # Imagen para el botón Datos
            "algorithms": PhotoImage(file="assets/ButtonAlgo.png"),# Imagen para el botón Algoritmos
            "logout": PhotoImage(file="assets/ButtonLogut.png"),        # Imagen para el botón Logout
        }

        # Mostrar el dashboard inicialmente
        show_dashboard(self.main_frame)

    def create_menu(self):
        # Configuración de los botones con imágenes y posiciones en la barra lateral
        buttons_info = [
            ("Dashboard", "dashboard", 50),
            ("Mapa", "maps", 110),
            ("Datos", "datos", 170),
            ("Algoritmos", "algorithms", 230),
            ("Logout", "logout", 350),
        ]

        # Crear los botones en la barra lateral
        for text, image_key, y_pos in buttons_info:
            button_image = self.button_images[image_key]
            button = tk.Button(
                self.sidebar_frame,
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda key=image_key: self.handle_btn_press(key),
                cursor='hand2',
                activebackground="#1e4bb8",
                relief="flat",
            )
            button.pack(pady=20)


    def handle_btn_press(self, btn_key):
        clear_frame(self.main_frame)
        if btn_key == "maps":
            show_map(self.main_frame)
        elif btn_key == "datos":
            show_data(self.main_frame)
        elif btn_key == "algorithms":
            show_algorithms(self.main_frame)
        elif btn_key == "dashboard":
            show_dashboard(self.main_frame)
        elif btn_key == "logout":
            self.parent.destroy()


        print(f"Botón '{btn_key}' presionado.")

# Inicializar la ventana principal
root = tk.Tk()
root.title("Optimización de Infraestructura de Distribución de Energía")
root.geometry("1200x600")  # Ajustar el tamaño de la ventana para que sea más grande

# Crear el menú lateral con los botones y la funcionalidad
app_menu = Menu(root)
app_menu.create_menu()
# Show the login window
login_window(root)
# Ejecutar la aplicación
root.mainloop()
