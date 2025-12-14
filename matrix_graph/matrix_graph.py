

class Vertice:
    def __init__(self,index : int = 0):
        self.index = index
    def __str__(self):
        return f"Vertice {self.index}"


class MatrixGraph:
    def __init__(self):
        self.number_of_vertices : int = 0
        self.vertices : list[Vertice] = []
        self.edge_matrix : list[list] = []

    def add_vertice(self,vertice : Vertice):
        if vertice in self.vertices:
            raise Exception("Graph already has this vertice")
        vertice.index = self.number_of_vertices
        self.number_of_vertices += 1
        self.vertices.append(vertice)
        for row in self.edge_matrix:
            row.append(0)
        self.edge_matrix.append([0 for _ in range(self.number_of_vertices)])


    def remove_vertice(self,vertice : Vertice):
        if vertice not in self.vertices:
            return
        for row in self.edge_matrix:
            del row[vertice.index - 1]
        del self.edge_matrix[vertice.index - 1]
        self.number_of_vertices -= 1
        for index in range(vertice.index,self.number_of_vertices):
            self.vertices[index].index -= 1
        self.vertices.remove(vertice)



    def add_vertices(self, vertices : list[Vertice]):
        for vertice in vertices:
            self.add_vertice(vertice)

    def remove_vertices(self, vertices : list[Vertice]):
        for vertice in vertices:
            self.remove_vertice(vertice)

    def add_edge(self, vertice_1 : Vertice, vertice_2 : Vertice):
        if not (vertice_1 in self.vertices and vertice_2 in self.vertices):
            print("Edge could not be constructed because vertices are not in graph")
            return
        self.edge_matrix[vertice_2.index][vertice_1.index] = 1
        self.edge_matrix[vertice_1.index][vertice_2.index] = 1

    def remove_edge(self, vertice_1 : Vertice, vertice_2 : Vertice):
        if not (vertice_1 in self.vertices and vertice_2 in self.vertices):
            print("Edge could not be removed because vertices are not in graph")
            return
        self.edge_matrix[vertice_2.index][vertice_1.index] = 0
        self.edge_matrix[vertice_1.index][vertice_2.index] = 0

    def add_edges(self,edges : list[tuple[Vertice,Vertice]]):
        for vertice_1,vertice_2 in edges:
            self.add_edge(vertice_1,vertice_2)

    def remove_edges(self,edges : list[tuple[Vertice,Vertice]]):
        for vertice_1,vertice_2 in edges:
            self.remove_edge(vertice_1,vertice_2)

    def show(self):
        #print(f"Number of vertices : {self.number_of_vertices}")
        #print(f"Vertices:",*self.vertices,"\n")
        for row in self.edge_matrix:
            print(*row)
