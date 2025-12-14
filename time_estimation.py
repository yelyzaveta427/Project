import time
from graph_generation import generate_simple_exact_graph

def estimate_algorithm_time(num_vertices,density,algorithm):
    print(f"Generation graph with V={num_vertices} та D={density}...")
    try:
        graph = generate_simple_exact_graph(num_vertices, density)
    except ValueError as error:
        print(f"Mistake of graph generation: {error}")

    start = time.time()
    result = algorithm(graph)
    end = time.time()
    execution_time = end - start
    return graph, result, execution_time