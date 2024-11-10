import tkinter as tk
from PIL import Image, ImageTk
from utils import clear_frame

def show_dashboard(main_frame):
    clear_frame(main_frame)
    
    # Set colors
    title_color = "#5F95FF"  # Blue color for main titles
    section_title_color = "#1c1c1c"  # Dark color for section titles
    text_color = "#333333"  # General text color

    # Set fonts
    title_font = ("Arial", 24, "bold")
    section_title_font = ("Arial", 18, "bold")
    text_font = ("Arial", 12)

    # Main title
    title = tk.Label(main_frame, text="Optimización de la Infraestructura\n de Distribución de Energía", 
                     font=title_font, fg=title_color, bg="white", justify="center")
    title.pack(pady=15)

    # Container frame for sections
    section_frame = tk.Frame(main_frame, bg="white", padx=10, pady=10)
    section_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Load images and create ImageTk objects
    image_1 = Image.open("assets/i1.jpg").resize((250, 150))
    image_2 = Image.open("assets/i2.jpg").resize((250, 150))
    img_1 = ImageTk.PhotoImage(image_1)
    img_2 = ImageTk.PhotoImage(image_2)

    # Text Section
    text_container = tk.Frame(section_frame, bg="white")
    text_container.pack(fill="x", pady=(0, 10))

    # Context Text
    subtitle_context = tk.Label(text_container, text="Contexto", font=section_title_font, fg=section_title_color, bg="white")
    subtitle_context.pack(anchor="w", pady=(5, 5))

    context_text = tk.Label(text_container, text="Adinelsa opera en zonas rurales y de difícil acceso en Perú, enfrentando desafíos "
                                                 "debido a su ubicación geográfica y la falta de infraestructura adecuada.",
                            font=text_font, fg=text_color, bg="white", wraplength=700, justify="left")
    context_text.pack(anchor="w")

    # Problem Text
    subtitle_problem = tk.Label(text_container, text="Fundamentación del Problema", font=section_title_font, fg=section_title_color, bg="white")
    subtitle_problem.pack(anchor="w", pady=(10, 5))

    problem_text = tk.Label(text_container, text="Conectar localidades rurales con energía eléctrica confiable es crucial. Adinelsa "
                                                 "enfrenta altos costos de operación por la dispersión geográfica de sus nodos y "
                                                 "variabilidad en las tarifas, complicando la distribución equitativa.",
                            font=text_font, fg=text_color, bg="white", wraplength=700, justify="left")
    problem_text.pack(anchor="w")

    # Solution Text
    subtitle_solution = tk.Label(text_container, text="Solución Propuesta", font=section_title_font, fg=section_title_color, bg="white")
    subtitle_solution.pack(anchor="w", pady=(10, 5))

    solution_text = tk.Label(text_container, text="Se propone implementar algoritmos de Árbol de Expansión Mínima (MST), como "
                                                  "Kruskal y Prim, para diseñar una red optimizada que minimice costos y garantice "
                                                  "cobertura eficiente, asegurando acceso económico a la energía.",
                             font=text_font, fg=text_color, bg="white", wraplength=700, justify="left")
    solution_text.pack(anchor="w")

    # Image Section
    image_container = tk.Frame(section_frame, bg="white")
    image_container.pack(fill="x", pady=(10, 0))

    # Image 1
    context_image = tk.Label(image_container, image=img_1, bg="white")
    context_image.image = img_1  # Keep a reference to prevent garbage collection
    context_image.pack(side="left", padx=10)

    # Image 2
    problem_image = tk.Label(image_container, image=img_2, bg="white")
    problem_image.image = img_2  # Keep a reference to prevent garbage collection
    problem_image.pack(side="left", padx=10)
