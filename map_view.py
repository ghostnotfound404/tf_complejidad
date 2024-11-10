import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def open_map_window():
    """
    Abre una nueva ventana que muestra el mapa de Perú con los puntos coloreados por departamento.
    """
    # Crear una nueva ventana para el mapa
    
    #map_window = tk.Toplevel()
    #map_window.title("Mapa de Localidades en Perú")
    #map_window.geometry("900x700")

    # Cargar el archivo CSV
    file_path = 'coordenadas.csv'  # Asegúrate de que esta ruta sea correcta
    df = pd.read_csv(file_path, encoding='latin1')
    df_clean = df.dropna(subset=['Latitud', 'Longitud'])

    # Asignar colores a los departamentos
    departments = df_clean['DEPARTAMENTO'].unique()
    colors = ['blue', 'purple', 'orange', 'green', 'red', 'pink', 'yellow', 'cyan', 'gray', 'brown']
    color_map = {dept: colors[i % len(colors)] for i, dept in enumerate(departments)}

    # Crear el gráfico utilizando Basemap
    plt.figure(figsize=(10, 8))
    m = Basemap(projection='merc', llcrnrlat=-20, urcrnrlat=0, llcrnrlon=-82, urcrnrlon=-68, resolution='i')
    m.drawcoastlines()
    m.drawcountries()
    m.drawmapboundary(fill_color='lightblue')
    m.fillcontinents(color='lightgray', lake_color='lightblue')
    m.drawparallels(range(-20, 1, 5), labels=[1, 0, 0, 0])
    m.drawmeridians(range(-82, -67, 5), labels=[0, 0, 0, 1])

    # Dibujar los puntos, coloreados por departamento
    for dept, color in color_map.items():
        dept_data = df_clean[df_clean['DEPARTAMENTO'] == dept]
        x, y = m(dept_data['Longitud'].values, dept_data['Latitud'].values)
        m.scatter(x, y, color=color, label=dept, s=100, edgecolors='black')

    # Agregar título y leyenda
    plt.title("Conexiones de Energía en Perú por Departamento")
    plt.legend(title="Departamentos", loc='upper right')
    plt.show()

def show_map(main_frame):
    """
    Muestra el botón para abrir el mapa en la interfaz principal.
    """
    # Limpiar el contenido anterior del frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Etiqueta de título
    title = tk.Label(main_frame, text="Mapa de Localidades", font=("Arial", 20, "bold"))
    title.pack(pady=10)

    # Botón para abrir el mapa
    map_button = tk.Button(main_frame, text="Abrir Mapa", command=open_map_window, font=("Arial", 14))
    map_button.pack(pady=20)
