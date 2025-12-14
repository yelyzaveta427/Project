from algotithm_realization import hasHamiltonianCycle
from time_estimation import estimate_algorithm_time
if __name__ == "__main__":

    V_TEST = 20
    P_TEST = 0.5

    generated_graph, path_exists, exec_time = estimate_algorithm_time(
        num_vertices=V_TEST,
        density=P_TEST,
        algorithm=hasHamiltonianCycle
    )

    print("Results of testing")
    print("\nGenerated graph (adjacency list)")

    MAX_VERTICES_TO_SHOW = 10

    if V_TEST <= MAX_VERTICES_TO_SHOW:
        for u, neighbors in generated_graph.items():
            print(f"Vertice {u}: {neighbors}")
    else:

        print(
            f"Graph has {V_TEST} vertices. Print adjacency list for first {MAX_VERTICES_TO_SHOW} vertices:")

        for u in range(MAX_VERTICES_TO_SHOW):
            if u in generated_graph:

                neighbors_list = generated_graph[u]
                if len(neighbors_list) > 10:
                    print(f"Vertice {u}: {neighbors_list[:10]}... (more {len(neighbors_list) - 10} neighbors)")
                else:
                    print(f"Vertice {u}: {neighbors_list}")
            else:
                print(f"Vertice {u}: []")


    print("\nEstimation of time of algorithm work")

    if path_exists:
        print("Gamiltonian path is found")
    else:
        print("Gamiltonian path is not found")

    print(f"⏱ Time of algorithm`s work: {exec_time:.6f} sec")
