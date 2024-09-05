"""
This interface represents a directed graph.
@author morin (http://opendatastructures.org/)
"""
class Graph:

    """
    A self(V, E) has a number of vertices that is fixed upon initialization.
    The number of edges grows with every successful call to add_edge.
    """
    def __init__(self, n):
        self._nb_vertices = n
        self._nb_edges = 0

    """
    Return the overall number of vertices in the graph.
    @return the # of vertices (int)
    """
    def nb_vertices(self):
        return self._nb_vertices

    """
    Return the overall number of edges in the graph.
    @return the # of edges (int)
    """
    def nb_edges(self):
        return self._nb_edges

    """
    Add the edge (i -> j) to G(V, E)
    Do nothing if it already exists
    @param i the id of the source node 
    @param j the id of the destination node
    """
    def add_edge(self, i, j):
        pass

    """
    Remove the edge (i -> j) from G(V, E)
    Do nothing if it doesn't exist
    @param i the id of the source node 
    @param j the id of the destination node
    """
    def remove_edge(self, i, j):
        pass

    """
    Check if the edge (i -> j) ∈ G(V, E)
    @param i the id of the source node 
    @param j the id of the destination node
    @return True if (i -> j) exists, False otherwise
    """
    def has_edge(self, i, j):
        pass

    """
    Return a list of all vertices j such that (i -> j) ∈ G(V, E)
    @param i the id of the source node 
    @return 
    """
    def out_edges(self, i):
        pass

    """
    Return a list of all vertices j such that (j -> i) ∈ G(V, E)
    @param i the id of the destination node
    @return 
    """
    def in_edges(self, i):
        pass

    """
    Return the number of edges that connect vertex i to any other vertex.
    @param i  the identifier of the vertex
    @return the number of outgoing edges on vertex i
    """
    def out_degree(self, i):
        pass

    """
    Return the number of edges that connect any other vertex to vertex i.
    @param i  the identifier of the vertex
    @return the number of ingoing edges on vertex i
    """
    def in_degree(self, i):
        pass

    """
    Produce a textual representation of the graph.
    @return the string representation of G(V, E)
    """

    def __str__(self):
        s = "(" + self.__class__.__name__ + ") "
        s += str(self.nb_vertices()) + " vertices, "
        s += str(self.nb_edges()) + " edges\n"
        for i in range(self._nb_vertices):
            s += str(i) + ":"
            for j in self.out_edges(i):
                s += " " + str(j)
            s += "\n"
        return s

    """
    Generate a randomly connected graph.
    """
    def randomly_connect(self):
        n = self.nb_vertices()
        import random
        for i in range(n): 
            for j in range(n): 
                rVal = random.randint(0, n-1)
                if ((i != j) and ((rVal == 0) or (rVal == i))): 
                    self.add_edge(i, j)

    """
    Generate a strongly connected graph. 
    The produced graph connects every vertex v to vertices v+1 and v+2.
    """
    def strongly_connect(self):
        n = self.nb_vertices()
        for k in range(n): 
            self.add_edge(k, (k + 1) % n)
            self.add_edge(k, (k + 2) % n)

    """
    Generate a mesh: a non-directed N*N grid where all neighbors are
    connected. Meshing can only work if the number of vertices is a square
    value. To produce a non-directed graph, every connection between two
    vertices A and B is represented by two edges (A->B) and (B->A)
    """
    def mesh(self):
        import math
        n = int(math.sqrt(self.nb_vertices()))
        for k in range(self.nb_vertices()):
            if (k % n > 0):
                self.add_edge(k, k - 1)
            if (k >= n):
                self.add_edge(k, k - n)
            if (k % n != n - 1):
                self.add_edge(k, k + 1)
            if (k < (n * (n - 1))):
                self.add_edge(k, k + n)