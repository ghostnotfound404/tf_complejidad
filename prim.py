import heapq

def prim_algorithm(graph, start_node):
    '''
    Implementación del algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST).
    :param graph: Un diccionario que representa un grafo con las conexiones y pesos.
                  Ejemplo: { 'A': [('B', 2), ('C', 3)], 'B': [('A', 2), ('C', 1)], 'C': [('A', 3), ('B', 1)] }
    :param start_node: Nodo inicial para comenzar el algoritmo.
    :return: Lista de aristas que forman el MST y el costo total.
    '''
    visited = set()
    mst_edges = []
    total_cost = 0

    # Usamos una cola de prioridad para seleccionar la arista de menor peso
    min_heap = [(0, start_node, None)]  # (peso, nodo_actual, nodo_anterior)

    while min_heap:
        weight, current_node, previous_node = heapq.heappop(min_heap)
        
        if current_node in visited:
            continue

        visited.add(current_node)
        
        # Si no es el primer nodo, añadimos la arista al MST
        if previous_node is not None:
            mst_edges.append((previous_node, current_node, weight))
            total_cost += weight

        # Añadir todas las aristas adyacentes del nodo actual al heap
        for neighbor, edge_weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))
    
    return mst_edges, total_cost
