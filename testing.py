from matrix_graph.random_graph_generator import generate_matrix_graph
from matrix_graph.matrix_algorithm import hamiltonian_cycle_finder
from algotithm_realization import hasHamiltonianCycle
import time

def generate_graphs(number_of_vertices : int,density : float):
    matrix_graph = generate_matrix_graph(number_of_vertices,density)
    list_graph = {}
    for vertice in matrix_graph.vertices:
        list_neighbours = filter(lambda x : matrix_graph.edge_matrix[vertice][x], matrix_graph.vertices)
        list_graph[vertice] = list_neighbours
    return list_graph,matrix_graph

def estimate_time(number_of_vertices : int, density : float):
    list_graph,matrix_graph = generate_graphs(number_of_vertices, density)

    list_graph_time_0 = time.perf_counter()
    hasHamiltonianCycle(list_graph)
    list_graph_time_1 = time.perf_counter()

    matrix_graph_time_0 = time.perf_counter()
    hamiltonian_cycle_finder(matrix_graph)
    matrix_graph_time_1 = time.perf_counter()

    print(f"\nList time {list_graph_time_1 - list_graph_time_0}")
    print(f"Matrix time {matrix_graph_time_1 - matrix_graph_time_0}\n")
    return list_graph_time_1 - list_graph_time_0,matrix_graph_time_1 - matrix_graph_time_0

numbers = [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
densitys = [0.05,0.1,0.15,0.2,0.25]
def get_statistic(density):
    for number in numbers:
        for experiment_index in range(20):
            list_time,matrix_time = estimate_time(number,density)
            with open(f"statistic_{number}_{density}.csv", "a") as file:
                file.write(f"{number},{density},{list_time},{matrix_time},\n")
