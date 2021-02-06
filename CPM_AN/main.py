from Graph import Graph


from Schedule import Machines
from Visualisation import drawGraph

if __name__ == '__main__':
    graph = Graph()
    graph.set_nodes("NodesA", "GraphA")
    drawGraph(graph, "GraphA")
    print(graph)
    print(Machines(graph))
