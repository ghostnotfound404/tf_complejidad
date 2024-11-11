import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from utils import clear_frame
from prim import prim_algorithm
from kruskal import kruskal_algorithm

# Cargar los datos desde el archivo CSV
def load_coordinates():
    file_path = 'coordenadas.csv'
    df = pd.read_csv(file_path, encoding='latin1')
    df_clean = df.dropna(subset=['Latitud', 'Longitud'])
    df_clean.drop_duplicates(subset=['Latitud', 'Longitud'], inplace=True)
    return df_clean

coordinates_df = load_coordinates()

def get_localities_by_department(department):
    dept_data = coordinates_df[coordinates_df['DEPARTAMENTO'] == department]
    return [f"Node {i+1}" for i in dept_data.index]

def show_algorithms(main_frame):
    clear_frame(main_frame)
    label = tk.Label(main_frame, text="Algoritmos", font=("Arial", 20))
    label.pack(pady=10)

    algorithm_var = tk.StringVar(value="Prim")

    tk.Radiobutton(main_frame, text="Prim", variable=algorithm_var, value="Prim").pack(pady=5)
    tk.Radiobutton(main_frame, text="Kruskal", variable=algorithm_var, value="Kruskal").pack(pady=5)

    label_department = tk.Label(main_frame, text="Seleccione un departamento:")
    label_department.pack(pady=5)
    department_combobox = ttk.Combobox(main_frame, values=coordinates_df['DEPARTAMENTO'].unique().tolist())
    department_combobox.pack(pady=5)

    label_origin = tk.Label(main_frame, text="Seleccione la localidad de origen:")
    label_origin.pack(pady=5)
    origin_combobox = ttk.Combobox(main_frame)
    origin_combobox.pack(pady=5)

    label_destination = tk.Label(main_frame, text="Seleccione la localidad de destino:")
    label_destination.pack(pady=5)
    destination_combobox = ttk.Combobox(main_frame)
    destination_combobox.pack(pady=5)

    def on_department_selected(event):
        department = department_combobox.get()
        localities = get_localities_by_department(department)
        origin_combobox['values'] = localities
        destination_combobox['values'] = localities

    department_combobox.bind("<<ComboboxSelected>>", on_department_selected)

    result_button = tk.Button(main_frame, text="Ver Resultado", command=lambda: show_result(
        algorithm_var.get(), department_combobox.get(), origin_combobox.get(), destination_combobox.get()
    ))
    result_button.pack(pady=10)

    graph_button = tk.Button(main_frame, text="Mostrar Gráfico", command=lambda: show_graph(
        algorithm_var.get(), department_combobox.get()
    ))
    graph_button.pack(pady=10)

def show_result(algorithm, department, origin, destination):
    if not department or not origin or not destination:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos antes de ejecutar.")
        return

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
    else:
        mst_edges, total_cost = kruskal_algorithm(vertices, edges)
        result_text = f"Árbol de Expansión Mínima (Kruskal)\nCosto Total: {total_cost}\nAristas: {mst_edges}"

    messagebox.showinfo("Resultado", result_text)

def show_graph(algorithm, department):
    dept_data = coordinates_df[coordinates_df['DEPARTAMENTO'] == department]
    positions = {f"Node {i+1}": (row['Longitud'], row['Latitud']) for i, row in dept_data.iterrows()}
    graph = {}
    for index, row in dept_data.iterrows():
        node = f"Node {index+1}"
        neighbors = dept_data[dept_data.index != index]
        graph[node] = [(f"Node {i+1}", ((row['Latitud'] - r['Latitud'])**2 + (row['Longitud'] - r['Longitud'])**2)**0.5)
                       for i, r in neighbors.iterrows()]

    vertices = list(graph.keys())
    edges = [(w, u, v) for u in graph for v, w in graph[u]]

    if algorithm == "Prim":
        mst_edges, _ = prim_algorithm(graph, list(positions.keys())[0])
    else:
        mst_edges, _ = kruskal_algorithm(vertices, edges)

    G = nx.Graph()
    G.add_nodes_from(positions)
    G.add_edges_from([(u, v) for u, v, _ in mst_edges])

    pos = {node: (positions[node][0], positions[node][1]) for node in G.nodes}
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='gray', node_size=500, edge_color='red', font_color='blue')
    plt.title(f"Gráfico del MST - {algorithm} - {department}")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
