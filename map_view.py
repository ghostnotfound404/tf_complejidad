import tkinter as tk
from PIL import Image, ImageTk
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

    # Set colors
    title_color = "#5F95FF"  # Blue color for main titles
    box_bg_colors = ["#E3F2FD", "#E8F5E9", "#F3E5F5"]
    border_color = "#D1D5DB"  # Soft gray for border


    # Set fonts
    title_font = ("Arial", 24, "bold")
    box_font = ("Arial", 18, "bold")

    # Etiqueta de título
    title = tk.Label(main_frame, text="Mapa de Localidades en Perú", 
                     font=title_font, fg=title_color, bg="white", justify="center")
    title.pack(pady=15)
    data_labels = [
        ("Departamentos", "9"),
        ("Nodos Activos", "+1500"),
        ("Localidades", "1,245")    ]
    # Crear los recuadros
    for i, (label, value) in enumerate(data_labels):
        frame = tk.Frame(
            main_frame, 
            bg=box_bg_colors[i], 
            padx=10, 
            pady=5, 
            highlightbackground=border_color,  # Color del borde
            highlightthickness=2,  # Grosor del borde
            highlightcolor=border_color  # Color del borde cuando está enfocado
        )
        frame.pack(pady=10, fill='x')

        lbl_label = tk.Label(frame, text=label, font=box_font, fg="black", bg=box_bg_colors[i], anchor="w")
        lbl_label.pack(side="left", padx=10)
        
        lbl_value = tk.Label(frame, text=value, font=box_font, fg="black", bg=box_bg_colors[i], anchor="e")
        lbl_value.pack(side="right", padx=10)

    # Cargar la imagen del botón
    button_image = Image.open("assets/ShowMap.png")
    button_image = button_image.resize((150, 50))  # Ajusta el tamaño de la imagen si es necesario
    button_photo = ImageTk.PhotoImage(button_image)

    # Botón para abrir el mapa con la imagen
    map_button = tk.Button(main_frame, image=button_photo, command=open_map_window, borderwidth=0)
    map_button.image = button_photo  # Guardar una referencia para evitar que se recoja como basura
    map_button.pack(pady=20)
