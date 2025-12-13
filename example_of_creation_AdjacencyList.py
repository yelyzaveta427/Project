class ListGraph:
    def __init__(self, vertices: list = None, edges: list = None):

        self.adj_list = {}
        if vertices:
            self._initialize_list(vertices)
        if edges:
            self._create_initial_list(edges)

    def _initialize_list(self, vertices: list):
        for vertex in vertices:
            self.adj_list[vertex] = []

    def _create_initial_list(self, edges: list):
        for u, v in edges:
            self.add_edge(u, v)

    def get_vertices(self) -> list:
        return list(self.adj_list.keys())

    def get_edges(self) -> list:
        edges = set()
        for u, neighbors in self.adj_list.items():
            for v in neighbors:
                edge = tuple(sorted((u, v)))
                edges.add(edge)
        return list(edges)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            print(f"Vertex '{vertex}' is added.")
        else:
            print(f"Vertex '{vertex}' already exists.")

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in list(self.adj_list[vertex]):
                if neighbor in self.adj_list:
                    self.adj_list[neighbor].remove(vertex)
            del self.adj_list[vertex]
            print(f"Vertex '{vertex}' and connected to it edges are removed.")
        else:
            print(f"Vertex '{vertex}' is not found.")

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

        print(f"Edge ({u}, {v}) is added.")

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            removed = False
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
                removed = True
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)
                removed = True

            if removed:
                print(f"Edge ({u}, {v}) is removed.")
            else:
                print(f"Edge ({u}, {v}) does not exist.")
        else:
            print("One vertice does not exist or both vertices do not exist.")

    def display(self):
        print("\nAdjacency list")
        for vertex, neighbors in self.adj_list.items():
            print(f"Vertice {vertex}: {neighbors}")


print("Initialization")
graph = ListGraph(
    vertices=['A', 'B', 'C', 'D'],
    edges=[('A', 'B'), ('B', 'C'), ('C', 'D')])
graph.display()

print("\nAdding vertice 'E'")
graph.add_vertex('E')
graph.display()

print("\nAdding edges (A, D) and (E, B)")
graph.add_edge('A', 'D')
graph.add_edge('E', 'B')
graph.display()

print("\nDeleting edges (B, C)")
graph.remove_edge('B', 'C')
graph.display()

print("\nDeleting vertice 'B'")
graph.remove_vertex('B')
graph.display()

print("\nAttempt to delete unexisting edge (A, C)")
graph.remove_edge('A', 'C')
