import tkinter as tk
from utils import clear_frame

def show_dashboard(main_frame):
    clear_frame(main_frame)
    
    # Título principal
    title = tk.Label(main_frame, text="Optimización de la Infraestructura\n de Distribución de Energía", font=("Arial", 24, "bold"))
    title.pack(pady=10)
    
    # Subtítulos y contenido
    subtitle_context = tk.Label(main_frame, text="Contexto", font=("Arial", 18, "bold"))
    subtitle_context.pack(anchor="w", padx=20, pady=5)

    context_text = tk.Label(main_frame, text=("Adinelsa opera en zonas rurales y de difícil acceso en Perú, enfrentando desafíos "
                                              "debido a su ubicación geográfica y la falta de infraestructura adecuada."),
                            font=("Arial", 12), justify="left", wraplength=600)
    context_text.pack(anchor="w", padx=20)

    subtitle_problem = tk.Label(main_frame, text="Fundamentación del Problema", font=("Arial", 18, "bold"))
    subtitle_problem.pack(anchor="w", padx=20, pady=5)

    problem_text = tk.Label(main_frame, text=("Conectar localidades rurales con energía eléctrica confiable es crucial. Adinelsa "
                                              "enfrenta altos costos de operación por la dispersión geográfica de sus nodos y "
                                              "variabilidad en las tarifas, complicando la distribución equitativa."),
                            font=("Arial", 12), justify="left", wraplength=600)
    problem_text.pack(anchor="w", padx=20)

    subtitle_solution = tk.Label(main_frame, text="Solución Propuesta", font=("Arial", 18, "bold"))
    subtitle_solution.pack(anchor="w", padx=20, pady=5)

    solution_text = tk.Label(main_frame, text=("Se propone implementar algoritmos de Árbol de Expansión Mínima (MST), como "
                                               "Kruskal y Prim, para diseñar una red optimizada que minimice costos y garantice "
                                               "cobertura eficiente, asegurando acceso económico a la energía."),
                             font=("Arial", 12), justify="left", wraplength=600)
    solution_text.pack(anchor="w", padx=20)

    # Espacio para las imágenes (si necesitas)
    placeholder_1 = tk.Label(main_frame, bg="lightgray", width=20, height=5)
    placeholder_1.pack(side="left", padx=50, pady=20)

    placeholder_2 = tk.Label(main_frame, bg="lightgray", width=20, height=5)
    placeholder_2.pack(side="left", padx=50, pady=20)
