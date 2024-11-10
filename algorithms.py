import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from utils import clear_frame  # Asumiendo que clear_frame está definido en utils.py

def show_algorithms(main_frame):
    clear_frame(main_frame)
    label = tk.Label(main_frame, text="Algoritmos", font=("Arial", 20))
    label.pack(pady=10)

    label_algorithm = tk.Label(main_frame, text="Seleccione el algoritmo:")
    label_algorithm.pack(pady=5)

    button_prim = tk.Button(main_frame, text="Prim", command=run_prim)
    button_prim.pack(pady=5)

    button_kruskal = tk.Button(main_frame, text="Kruskal", command=run_kruskal)
    button_kruskal.pack(pady=5)

    # Selección de departamento
    label_department = tk.Label(main_frame, text="Seleccione un departamento:")
    label_department.pack(pady=5)
    
    department_combobox = ttk.Combobox(main_frame, values=["Amazonas", "Áncash", "Apurímac", "Arequipa"])
    department_combobox.pack(pady=5)

    # Selección de localidades
    label_origin = tk.Label(main_frame, text="Seleccione la localidad de origen:")
    label_origin.pack(pady=5)
    
    origin_combobox = ttk.Combobox(main_frame)
    origin_combobox.pack(pady=5)

    label_destination = tk.Label(main_frame, text="Seleccione la localidad de destino:")
    label_destination.pack(pady=5)
    
    destination_combobox = ttk.Combobox(main_frame)
    destination_combobox.pack(pady=5)

    # Cargar la imagen del botón
    execute_image = Image.open("assets/execute.png")
    execute_image = execute_image.resize((150, 50))  # Ajusta el tamaño según sea necesario
    execute_photo = ImageTk.PhotoImage(execute_image)

    execute_button = tk.Button(main_frame, image=execute_photo, command=lambda: execute_algorithm(
        department_combobox.get(),
        origin_combobox.get(),
        destination_combobox.get()
    ), borderwidth=0)
    execute_button.image = execute_photo  # Guardar referencia para evitar recolección de basura
    execute_button.pack(pady=10)

    # Vincular la selección de departamentos para cargar localidades
    def on_department_selected(event):
        department = department_combobox.get()
        # Aquí, deberías cargar localidades según el departamento
        localidades = {"Amazonas": ["Localidad A", "Localidad B"],
                       "Áncash": ["Localidad C", "Localidad D"],
                       "Apurímac": ["Localidad E", "Localidad F"],
                       "Arequipa": ["Localidad G", "Localidad H"]}
        origin_combobox['values'] = localidades.get(department, [])
        destination_combobox['values'] = localidades.get(department, [])

    department_combobox.bind("<<ComboboxSelected>>", on_department_selected)

def run_prim():
    messagebox.showinfo("Prim", "Ejecutando el algoritmo de Prim")

def run_kruskal():
    messagebox.showinfo("Kruskal", "Ejecutando el algoritmo de Kruskal")

def execute_algorithm(department, origin, destination):
    if not department or not origin or not destination:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos antes de ejecutar.")
    else:
        messagebox.showinfo("Ejecutar", f"Ejecutando algoritmo para {origin} a {destination} en {department}")
