from graphADT import Graph

"""An implementation of the adjacency matrix representation of a graph"""


class AdjacencyMatrixGraph(Graph):

    def __init__(self, n):
        super().__init__(n)
        self._initialize()
                
    def _initialize(self):
        am = []
        n = self.nb_vertices()
        for i in range(n):
            am.append([False] * n)
        self._adj_matrix = am

    def add_edge(self, i, j):
        if (not self._adj_matrix[i][j]):
            self._nb_edges += 1
            self._adj_matrix[i][j] = True

    def remove_edge(self, i, j):
        if (self._adj_matrix[i][j]):
            self._nb_edges -= 1
            self._adj_matrix[i][j] = False

    def has_edge(self, i, j):
        return self._adj_matrix[i][j]

    def in_edges(self, i):
        out = list()
        for j in range(self.n):
            if self._adj_matrix[j][i]:
                out.append(j)
        return out
        
    def in_degree(self, i):
        deg = 0
        for j in range(self.n):
            if self._adj_matrix[j][i]:
                deg += 1
        return deg

    def out_edges(self, i):
        out = list()
        for j in range(self.nb_vertices()):
            if self._adj_matrix[i][j]:
                out.append(j)
        return out

    def out_degree(self, i):
        deg = 0
        for j in range(self.nb_vertices()):
            if self._adj_matrix[i][j]:
                deg += 1
        return deg
