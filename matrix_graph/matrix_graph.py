


class MatrixGraph:
    def __init__(self):
        self.number_of_vertices : int = 0
        self.vertices : list[int] = []
        self.edge_matrix : list[list] = []

    def add_vertice(self):
        self.vertices.append(self.number_of_vertices)
        self.number_of_vertices += 1
        for row in self.edge_matrix:
            row.append(0)
        self.edge_matrix.append([0 for _ in range(self.number_of_vertices)])


    def remove_vertice(self,vertice : int):
        if vertice not in self.vertices:
            return
        for row in self.edge_matrix:
            del row[vertice - 1]
        del self.edge_matrix[vertice - 1]
        self.number_of_vertices -= 1
        for index in range(vertice,self.number_of_vertices):
            self.vertices[index] -= 1
        self.vertices.remove(vertice)



    def add_vertices(self, vertices : int):
        for vertice in range(vertices):
            self.add_vertice()

    def remove_vertices(self, vertices : list[int]):
        for vertice in vertices:
            self.remove_vertice(vertice)

    def add_edge(self, vertice_1 : int, vertice_2 : int):
        if not (vertice_1 in self.vertices and vertice_2 in self.vertices):
            print("Edge could not be constructed because vertices are not in graph")
            return
        self.edge_matrix[vertice_2][vertice_1] = 1
        self.edge_matrix[vertice_1][vertice_2] = 1

    def remove_edge(self, vertice_1 : int, vertice_2 : int):
        if not (vertice_1 in self.vertices and vertice_2 in self.vertices):
            print("Edge could not be removed because vertices are not in graph")
            return
        self.edge_matrix[vertice_2][vertice_1] = 0
        self.edge_matrix[vertice_1][vertice_2] = 0

    def add_edges(self,edges : list[tuple[int,int]]):
        for vertice_1,vertice_2 in edges:
            self.add_edge(vertice_1,vertice_2)

    def remove_edges(self,edges : list[tuple[int,int]]):
        for vertice_1,vertice_2 in edges:
            self.remove_edge(vertice_1,vertice_2)

    def show(self):
        #print(f"Number of vertices : {self.number_of_vertices}")
        #print(f"Vertices:",*self.vertices,"\n")
        for row in self.edge_matrix:
            print(*row)
