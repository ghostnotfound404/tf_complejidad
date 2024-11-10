import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Toplevel
from utils import clear_frame

def show_map(main_frame):
    clear_frame(main_frame)
    button_prim = tk.Button(
        main_frame,
        text="Maps",
        font=("Arial", 10),
        width=10,
        height=3,
        command=run_maps  # Asigna la función `run_maps` al botón
    )
    button_prim.place(relx=0.5, rely=0.4, anchor="center")

""" def run_maps():
    # Crear una nueva ventana para el mapa
    map_window = Toplevel()
    map_window.title("Conexiones de Energía en Perú por Departamento")
    map_window.geometry("800x600")

    # Cargar datos geográficos de Perú
    peru_gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    peru_gdf = peru_gdf[peru_gdf.name == "Peru"]

    # Crear una lista de coordenadas para los departamentos
    departamentos = {
        "ANCASH": (-77.45, -9.33),
        "AREQUIPA": (-71.53, -16.40),
        "AYACUCHO": (-74.22, -13.16),
        "CAJAMARCA": (-78.52, -7.16),
        "HUANCAVELICA": (-75.02, -12.78),
        "ICA": (-75.20, -14.07),
        "LIMA": (-76.99, -12.04),
        "LORETO": (-74.67, -4.07),
        "PASCO": (-75.34, -10.68)
    }
    
    # Crear un grafo de networkx y añadir nodos y conexiones
    G = nx.Graph()
    for depto, coords in departamentos.items():
        G.add_node(depto, pos=coords)
    
    # Añadir algunas conexiones manualmente entre departamentos
    conexiones = [
        ("LIMA", "ANCASH"), ("LIMA", "ICA"), ("LIMA", "HUANCAVELICA"),
        ("AYACUCHO", "HUANCAVELICA"), ("AREQUIPA", "ICA"), ("LORETO", "PASCO"),
        ("CAJAMARCA", "ANCASH"), ("PASCO", "ANCASH")
    ]
    G.add_edges_from(conexiones)
    
    # Crear la figura de matplotlib
    fig, ax = plt.subplots(figsize=(8, 8))
    peru_gdf.plot(ax=ax, color="white", edgecolor="blue")

    # Dibujar los nodos y las conexiones
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="gray", width=1)
    nx.draw_networkx_nodes(
        G, pos, ax=ax, node_size=50,
        node_color=["blue", "purple", "red", "orange", "yellow", "green", "pink", "gray", "magenta"]
    )
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=8, font_color="black")
    
    # Personalizar el gráfico
    ax.set_title("Conexiones de Energía en Perú por Departamento")
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    
    # Crear una leyenda manual
    colores = ["blue", "purple", "red", "orange", "yellow", "green", "pink", "gray", "magenta"]
    etiquetas = list(departamentos.keys())
    for color, label in zip(colores, etiquetas):
        ax.scatter([], [], c=color, label=label)
    ax.legend(title="Departamentos", loc="upper right")
    
    # Incrustar la figura en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=map_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Importante: cerrar la figura después de incrustarla en Tkinter para evitar problemas de memoria
    plt.close(fig)
 """