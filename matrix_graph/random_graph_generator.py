import random
from .matrix_graph import MatrixGraph
def generate_matrix_graph(number_of_vertices : int, density : float):
    max_number_of_edges = number_of_vertices * (number_of_vertices - 1) // 2
    number_of_edges = int(max_number_of_edges * min(1,density))
    number_of_generated_edges = 0
    graph = MatrixGraph()
    graph.add_vertices(number_of_vertices)
    while number_of_generated_edges < number_of_edges:
        vertice_index_1 = random.randint(0,number_of_vertices - 1)
        vertice_index_2 = random.randint(0,number_of_vertices - 1)
        if vertice_index_1 == vertice_index_2: continue
        if graph.edge_matrix[vertice_index_1][vertice_index_2] == 1: continue
        graph.edge_matrix[vertice_index_1][vertice_index_2] = 1
        graph.edge_matrix[vertice_index_2][vertice_index_1] = 1
        number_of_generated_edges += 1
    return graph
