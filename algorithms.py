import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pandas as pd
from utils import clear_frame
from prim import prim_algorithm
from kruskal import kruskal_algorithm

# Cargar los datos desde el archivo CSV
def load_coordinates():
    file_path = 'coordenadas.csv'
    df = pd.read_csv(file_path, encoding='latin1')
    df_clean = df.dropna(subset=['Latitud', 'Longitud'])
    return df_clean

coordinates_df = load_coordinates()

def get_localities_by_department(department):
    """
    Devuelve una lista de nodos (puntos) para un departamento dado.
    """
    dept_data = coordinates_df[coordinates_df['DEPARTAMENTO'] == department]
    return [f"Node {i+1}" for i in dept_data.index]

def show_algorithms(main_frame):
    clear_frame(main_frame)
    label = tk.Label(main_frame, text="Algoritmos", font=("Arial", 20))
    label.pack(pady=10)

    label_algorithm = tk.Label(main_frame, text="Seleccione el algoritmo:")
    label_algorithm.pack(pady=5)

    # Variable para el algoritmo seleccionado
    algorithm_var = tk.StringVar(value="Prim")

    button_prim = tk.Radiobutton(main_frame, text="Prim", variable=algorithm_var, value="Prim")
    button_prim.pack(pady=5)

    button_kruskal = tk.Radiobutton(main_frame, text="Kruskal", variable=algorithm_var, value="Kruskal")
    button_kruskal.pack(pady=5)

    # Selección de departamento
    label_department = tk.Label(main_frame, text="Seleccione un departamento:")
    label_department.pack(pady=5)
    
    department_combobox = ttk.Combobox(main_frame, values=coordinates_df['DEPARTAMENTO'].unique().tolist())
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
    execute_image = execute_image.resize((150, 50))
    execute_photo = ImageTk.PhotoImage(execute_image)

    execute_button = tk.Button(main_frame, image=execute_photo, command=lambda: execute_algorithm(
        algorithm_var.get(),
        department_combobox.get(),
        origin_combobox.get(),
        destination_combobox.get()
    ), borderwidth=0)
    execute_button.image = execute_photo
    execute_button.pack(pady=10)

    # Función para actualizar localidades según el departamento seleccionado
    def on_department_selected(event):
        department = department_combobox.get()
        localities = get_localities_by_department(department)
        origin_combobox['values'] = localities
        destination_combobox['values'] = localities

    department_combobox.bind("<<ComboboxSelected>>", on_department_selected)

def execute_algorithm(algorithm, department, origin, destination):
    if not department or not origin or not destination:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos antes de ejecutar.")
        return

    # Crear el grafo basado en las coordenadas cargadas
    dept_data = coordinates_df[coordinates_df['DEPARTAMENTO'] == department]
    graph = {}
    for index, row in dept_data.iterrows():
        node = f"Node {index+1}"
        neighbors = dept_data[dept_data.index != index]
        graph[node] = [(f"Node {i+1}", ((row['Latitud'] - r['Latitud'])**2 + (row['Longitud'] - r['Longitud'])**2)**0.5)
                       for i, r in neighbors.iterrows()]

    vertices = list(graph.keys())
    edges = [(w, u, v) for u in graph for v, w in graph[u]]

    if algorithm == "Prim":
        mst_edges, total_cost = prim_algorithm(graph, origin)
        result_text = f"Árbol de Expansión Mínima (Prim)\nCosto Total: {total_cost}\nAristas: {mst_edges}"
    elif algorithm == "Kruskal":
        mst_edges, total_cost = kruskal_algorithm(vertices, edges)
        result_text = f"Árbol de Expansión Mínima (Kruskal)\nCosto Total: {total_cost}\nAristas: {mst_edges}"
    else:
        result_text = "Algoritmo no válido seleccionado."

    messagebox.showinfo("Resultado", result_text)
