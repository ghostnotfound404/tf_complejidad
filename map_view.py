import pandas as pd
import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk

class MapView:
    def __init__(self, parent):
        self.parent = parent

    def show_map_button(self):
        map_button = tk.Button(
            self.parent,
            text="Mostrar Mapa",
            command=self.plot_map
        )
        map_button.place(x=500, y=170)  # Ajusta la posición según sea necesario

    def plot_map(self):
        # Cargar el CSV con localidades
        df = pd.read_csv('/mnt/data/consumo_adinelsa_202305_0 (1).csv', encoding='ISO-8859-1', delimiter=';')

        # Crear un grafo
        G = nx.Graph()

        # Diccionario de colores para los departamentos
        departamentos_colores = {
            'ANCASH': 'blue',
            'AREQUIPA': 'purple',
            'AYACUCHO': 'orange',
            'CAJAMARCA': 'pink',
            'HUANCAVELICA': 'yellow',
            'ICA': 'green',
            'LIMA': 'red',
            'LORETO': 'magenta',
            'PASCO': 'gray'
        }

        # Añadir nodos al grafo
        for _, row in df.iterrows():
            G.add_node(row['LOCALIDAD'], 
                       departamento=row['DEPARTAMENTO'], 
                       consumo=row['CONSUMO_KW'], 
                       pos=(row['Longitud'], row['Latitud']))  # Asegúrate de que existan las columnas 'Longitud' y 'Latitud'

        # Conectar localidades basándose en el CSV
        for _, row in df.iterrows():
            connected_localities = row.get('ConectadoA')  # Obtener localidades conectadas
            if isinstance(connected_localities, str):  # Verificar si es una cadena
                connected_localities = connected_localities.split(';')  # Dividir si es una cadena
                for locality in connected_localities:
                    G.add_edge(row['LOCALIDAD'], locality.strip())  # Añadir la conexión al grafo

        # Cargar el mapa de Perú desde geopandas
        peru = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        peru = peru[peru.name == "Peru"]

        # Crear un GeoDataFrame para los nodos
        nodes_df = pd.DataFrame(G.nodes(data=True), columns=['Localidad', 'Data'])
        nodes_df['departamento'] = nodes_df['Data'].apply(lambda x: x['departamento'])
        nodes_gdf = gpd.GeoDataFrame(nodes_df, geometry=gpd.points_from_xy(nodes_df['Data'].apply(lambda x: x['pos'][0]),
                                                                            nodes_df['Data'].apply(lambda x: x['pos'][1])))

        # Dibujar el mapa
        fig, ax = plt.subplots(figsize=(12, 12))
        peru.boundary.plot(ax=ax, linewidth=1)  # Dibujar fronteras de Perú

        # Dibujar localidades con colores por departamento
        for dep, color in departamentos_colores.items():
            local_nodes = nodes_df[nodes_df['departamento'] == dep]  # Filtrar localidades por departamento
            ax.scatter(local_nodes['Data'].apply(lambda x: x['pos'][0]),  # Longitudes
                       local_nodes['Data'].apply(lambda x: x['pos'][1]),  # Latitudes
                       color=color, label=dep, s=50)  # Ajusta el tamaño de los puntos (s)

        # Dibujar el grafo
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.5, edge_color='black')

        # Ajustar la leyenda para que esté fuera del mapa
        plt.legend(title='Departamentos', bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.title('Conexiones de Energía en Perú por Departamento')
        plt.xlabel('Longitud')
        plt.ylabel('Latitud')
        plt.grid()
        plt.tight_layout()  # Ajustar el diseño para que no haya superposición
        plt.show()
