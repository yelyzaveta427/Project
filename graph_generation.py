import random
def generate_simple_exact_graph(num_vertices,density):

    if density < 0.0 or density > 1.0 or num_vertices <= 0:
        return {}
    if num_vertices == 1:
        return {0: []}
    edges = int(num_vertices * (num_vertices - 1) // 2)
    target_edges = density * edges
    adjacency_list = {}
    for i in range(num_vertices):
        adjacency_list[i] = []
    existing_edges = set()
    num_of_edges = 0
    while num_of_edges < target_edges:
        u = random.randrange(num_vertices)
        v = random.randrange(num_vertices)
        if u == v:
            continue
        if u > v:
            u, v = v, u
        new_edge = (u, v)
        if new_edge not in existing_edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            existing_edges.add(new_edge)
            num_of_edges += 1

    return adjacency_list