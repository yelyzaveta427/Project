from .matrix_graph import MatrixGraph
from .random_graph_generator import generate_matrix_graph
import copy
import math

def hamiltonian_cycle_finder(graph : MatrixGraph) -> bool:
    path_vertice = []
    for i in range(2 ** graph.number_of_vertices):
        path_vertice.append([False for _ in range(graph.number_of_vertices)])

    path_vertice[1 << 0][0] = True
    for binary_path in range(1,2 ** graph.number_of_vertices):

        for vertice_index in range(graph.number_of_vertices):
            if binary_path & (1 << vertice_index) != 0:
                previous_binary_path = binary_path ^ (1 << vertice_index)
                if previous_binary_path == 0: continue

                for u_vertice in filter(lambda x: graph.edge_matrix[x][vertice_index],graph.vertices):
                    if not graph.edge_matrix[u_vertice][vertice_index]:
                        continue
                    if previous_binary_path & (1 << u_vertice) == 0:
                        continue
                    if not path_vertice[previous_binary_path][u_vertice]:
                        continue
                    path_vertice[binary_path][vertice_index] = True
                    break
    full_path = (1 << graph.number_of_vertices) - 1
    for vertice in range(graph.number_of_vertices):
        if path_vertice[full_path][vertice] and graph.edge_matrix[0][vertice]:
            return True
    return False
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    graph = generate_matrix_graph(7,0.5)
    answer = hamiltonian_cycle_finder(graph)
    print(answer)
    # Define graph structure
    if answer or not answer:
        graph.show()
        nodes = {}
        for vertice in graph.vertices:
            angle = 2 * math.pi * vertice / graph.number_of_vertices
            x = 5 * math.cos(angle)
            y = 5 * math.sin(angle)
            nodes[vertice] = (x, y)

        edges = []
        for vertice_1 in graph.vertices:
            for vertice_2 in graph.vertices:
                if graph.edge_matrix[vertice_1][vertice_2]:
                    edges.append((vertice_1,vertice_2))

        # Draw edges
        for u, v in edges:
            x_values = [nodes[u][0], nodes[v][0]]
            y_values = [nodes[u][1], nodes[v][1]]
            plt.plot(x_values, y_values)

        # Draw nodes
        for node, (x, y) in nodes.items():
            plt.scatter(x, y)
            plt.text(x + 0.03, y + 0.03, str(node), fontsize=10)

        plt.title(f"{answer}")
        plt.axis("off")
        plt.show()
