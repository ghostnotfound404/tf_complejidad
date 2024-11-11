class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_algorithm(vertices, edges):
    '''
    Implementación del algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST).
    :param vertices: Lista de nodos (vértices) en el grafo.
    :param edges: Lista de aristas con formato (peso, nodo1, nodo2).
    :return: Lista de aristas que forman el MST y el costo total.
    '''
    disjoint_set = DisjointSet(vertices)
    mst_edges = []
    total_cost = 0

    # Ordenar las aristas por peso
    edges.sort()

    for weight, node1, node2 in edges:
        if disjoint_set.find(node1) != disjoint_set.find(node2):
            disjoint_set.union(node1, node2)
            mst_edges.append((node1, node2, weight))
            total_cost += weight

    return mst_edges, total_cost
