import tkinter as tk
from tkinter import ttk
import pandas as pd
from utils import clear_frame

def show_data(main_frame):
    clear_frame(main_frame)
# Set colors
    title_color = "#5F95FF"  # Blue color for main titles
    # Set fonts
    title_font = ("Arial", 24, "bold")
    # Main title
    title = tk.Label(main_frame, text="Datos de Consumo de Energía", 
                     font=title_font, fg=title_color, bg="white", justify="center")
    title.pack(pady=15)

    # Cargar los datos desde un CSV
    df = pd.read_csv('consumo_adinelsa_202305_0 (1).csv', encoding='latin1', sep=';')

    # Crear un frame que contendrá la tabla de datos
    table_frame = tk.Frame(main_frame)
    table_frame.pack(fill="both", expand=True)

    # Crear un Treeview para mostrar los datos
    tree = ttk.Treeview(table_frame, columns=list(df.columns), show="headings")
    tree.pack(fill="both", expand=True)

    # Configurar las columnas
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", minwidth=0, width=100)

    # Insertar los datos en la tabla
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))

    # Hacer que las barras de desplazamiento aparezcan si es necesario
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
