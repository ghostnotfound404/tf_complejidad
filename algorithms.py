import tkinter as tk
from tkinter import messagebox
from utils import clear_frame

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

def run_prim():
    messagebox.showinfo("Prim", "Ejecutando el algoritmo de Prim")

def run_kruskal():
    messagebox.showinfo("Kruskal", "Ejecutando el algoritmo de Kruskal")
