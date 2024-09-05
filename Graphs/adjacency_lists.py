from graphADT import Graph

"""An implementation of the adjacency list representation of a graph"""


class AdjacencyListsGraph(Graph):

    def __init__(self, n):
        super().__init__(n)
        self._initialize()
        
    def _initialize(self):
        self._adj_lists = []
        for i in range(self.nb_vertices()):
            self._adj_lists.append([])
            
    def add_edge(self, i, j):
        edges = self._adj_lists[i]
        if (j not in edges):
            edges.append(j)
            self._nb_edges += 1

    def remove_edge(self, i, j):
        edges = self._adj_lists[i]
        if (j in edges):
            edges.remove(j)
            self._nb_edges -= 1

    def has_edge(self, i, j):
        return (j in self._adj_lists[i])
        
    def out_edges(self, i):
        return self._adj_lists[i]

    def out_degree(self, i):
        return len(self._adj_lists[i])
        
    def in_edges(self, i):
        out = []
        for j in range(self._nb_vertices):
            if self.has_edge(j, i):
                out.append(j)
        return out
        
    def in_degree(self, i):
        deg = 0
        for j in range(self.n):
            if self.has_edge(j, i):
                deg += 1
        return deg

