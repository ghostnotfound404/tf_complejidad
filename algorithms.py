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
    df_clean = df.drop_duplicates(subset=['Latitud', 'Longitud']).dropna(subset=['Latitud', 'Longitud'])
    return df_clean

coordinates_df = load_coordinates()

def get_localities_by_department(department):
    dept_data = coordinates_df[coordinates_df['DEPARTAMENTO'] == department]
    return [f"Node {index+1}" for index in dept_data.index]

def adjust_positions(positions):
    adjusted = {}
    offset = 0.001  # Ajuste pequeño para evitar superposición
    seen_coords = {}
    for node, (x, y) in positions.items():
        if (x, y) in seen_coords:
            x += offset * seen_coords[(x, y)]
            y += offset * seen_coords[(x, y)]
            seen_coords[(x, y)] += 1
        else:
            seen_coords[(x, y)] = 1
        adjusted[node] = (x, y)
    return adjusted

def filter_relevant_edges(mst_edges, origin, destination):
    relevant_edges = []
    visited = set()
    stack = [origin]
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for edge in mst_edges:
                if current in edge[:2]:
                    relevant_edges.append(edge)
                    next_node = edge[1] if edge[0] == current else edge[0]
                    if next_node not in visited:
                        stack.append(next_node)
        if destination in visited:
            break

    return relevant_edges

def show_algorithms(main_frame):
    clear_frame(main_frame)

    title_color = "#5F95FF"  
    title_font = ("Arial", 24, "bold")
    subtitle_font = ("Arial", 15, "bold")

    label = tk.Label(main_frame, text="Algoritmos", font=title_font, fg=title_color, bg="white", justify="center")
    label.pack(pady=10)

    algorithm_var = tk.StringVar(value="Prim")

    tk.Radiobutton(main_frame, text="Prim", variable=algorithm_var, value="Prim", bg="white", font=subtitle_font).pack(pady=5)
    tk.Radiobutton(main_frame, text="Kruskal", variable=algorithm_var, value="Kruskal", bg="white", font=subtitle_font).pack(pady=5)

    label_department = tk.Label(main_frame, text="Seleccione un departamento:", bg="white")
    label_department.pack(pady=5)
    department_combobox = ttk.Combobox(main_frame, values=coordinates_df['DEPARTAMENTO'].unique().tolist())
    department_combobox.pack(pady=5)

    label_origin = tk.Label(main_frame, text="Seleccione la localidad de origen:", bg="white")
    label_origin.pack(pady=5)
    origin_combobox = ttk.Combobox(main_frame)
    origin_combobox.pack(pady=5)

    label_destination = tk.Label(main_frame, text="Seleccione la localidad de destino:", bg="white")
    label_destination.pack(pady=5)
    destination_combobox = ttk.Combobox(main_frame)
    destination_combobox.pack(pady=5)

    def on_department_selected(event):
        department = department_combobox.get()
        localities = get_localities_by_department(department)
        origin_combobox['values'] = localities
        destination_combobox['values'] = localities

    department_combobox.bind("<<ComboboxSelected>>", on_department_selected)

    ver_resultado_image = ImageTk.PhotoImage(Image.open("assets/view.png"))
    mostrar_grafico_image = ImageTk.PhotoImage(Image.open("assets/execute.png"))

    result_button = tk.Button(main_frame, image=ver_resultado_image, command=lambda: show_result(
        algorithm_var.get(), department_combobox.get(), origin_combobox.get(), destination_combobox.get()
    ))
    result_button.pack(pady=10)

    graph_button = tk.Button(main_frame, image=mostrar_grafico_image, command=lambda: show_graph(
        algorithm_var.get(), department_combobox.get(), origin_combobox.get(), destination_combobox.get()
    ))
    graph_button.pack(pady=10)

    main_frame.ver_resultado_image = ver_resultado_image
    main_frame.mostrar_grafico_image = mostrar_grafico_image

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

    if origin not in graph or destination not in graph:
        messagebox.showerror("Error", "El nodo seleccionado no existe en el grafo.")
        return

    vertices = list(graph.keys())
    edges = [(w, u, v) for u in graph for v, w in graph[u]]

    if algorithm == "Prim":
        mst_edges, total_cost = prim_algorithm(graph, origin)
    else:
        mst_edges, total_cost = kruskal_algorithm(vertices, edges)

    relevant_edges = filter_relevant_edges(mst_edges, origin, destination)
    relevant_nodes = set([node for edge in relevant_edges for node in edge[:2]])

    result_text = f"Árbol de Expansión Mínima ({algorithm})\n"
    result_text += f"Nodos incluidos: {', '.join(relevant_nodes)}\n"
    result_text += f"Costo Total: {total_cost}\n"
    result_text += f"Conexiones: {relevant_edges}"
    messagebox.showinfo("Resultado", result_text)

def show_graph(algorithm, department, origin, destination):
    dept_data = coordinates_df[coordinates_df['DEPARTAMENTO'] == department]
    positions = {f"Node {index+1}": (row['Longitud'], row['Latitud']) for index, row in dept_data.iterrows()}
    graph = {}

    for index, row in dept_data.iterrows():
        node = f"Node {index+1}"
        neighbors = dept_data[dept_data.index != index]
        graph[node] = [(f"Node {i+1}", ((row['Latitud'] - r['Latitud'])**2 + (row['Longitud'] - r['Longitud'])**2)**0.5)
                       for i, r in neighbors.iterrows()]

    if origin not in graph or destination not in graph:
        messagebox.showerror("Error", "El nodo seleccionado no existe en el grafo.")
        return

    if algorithm == "Prim":
        mst_edges, _ = prim_algorithm(graph, origin)
    else:
        mst_edges, _ = kruskal_algorithm(list(graph.keys()), [(w, u, v) for u in graph for v, w in graph[u]])

    relevant_edges = filter_relevant_edges(mst_edges, origin, destination)
    relevant_nodes = set([node for edge in relevant_edges for node in edge[:2]])

    G = nx.Graph()
    G.add_nodes_from(relevant_nodes)
    G.add_edges_from([(u, v) for u, v, _ in relevant_edges])  # Sin pesos

    pos = adjust_positions({node: positions[node] for node in relevant_nodes})

    plt.figure(figsize=(12, 8))
    nx.draw(
        G, pos, with_labels=True, node_color='#A9D0F5', node_size=1000, font_size=10,
        edge_color='black', width=2
    )
    plt.title(f"Recorrido del Nodo {origin} al Nodo {destination} ({algorithm})")
    plt.grid(False)
    plt.axis('off')
    plt.show()
