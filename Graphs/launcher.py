from adjacency_matrix import AdjacencyMatrixGraph
from adjacency_lists import AdjacencyListsGraph
import graph_algorithms


def main():

    print(" *** INIT ***\n")

    print("Random connections graph with 5 vertices")
    rcg = AdjacencyMatrixGraph(5)
    rcg.randomly_connect()
    print(rcg)
    print("Strongly connected graph with 9 vertices")
    scg = AdjacencyMatrixGraph(9)
    scg.strongly_connect()
    print(scg)
    print("Mesh graph with 9 vertices")
    mg = AdjacencyListsGraph(9)
    mg.mesh()
    print(mg)

    print("\n *** GRAPH EXPLORATION ***\n")

    print("BFS of the mesh")
    print(graph_algorithms.bfs(mg, 0))
    print("DFS of the mesh")
    print(graph_algorithms.iterativeDFS(mg, 0))
    print(graph_algorithms.recursiveDFS(mg, 0))

    print("\n *** GRAPH CONNECTIVITY ***\n")

    print("Connectivity graph of mesh graph")
    cg = graph_algorithms.computeConnectivity(mg)
    print(cg)
    print("Connectivity graph of strongly connected graph")
    cg = graph_algorithms.computeConnectivity(scg)
    print(cg)

    print("\n *** MINIMUM SPANNING TREES ***\n")

    print("Minimum Spanning Tree of mesh from V0")
    mst = graph_algorithms.computeMinimumSpanningTree(mg, 0)
    print(mst)
    print("Minimum Spanning Tree of SCG from V0")
    mst = graph_algorithms.computeMinimumSpanningTree(scg, 0)
    print(mst)

main()