from Graph import Graph
from Schedule import Schedule
from Visualisation import drawGraph

if __name__ == '__main__':
    graph = Graph()
    graph.set_nodes("GraphA")
    schedule = Schedule(graph)
    testGraph = graph
    drawGraph(testGraph, "GraphA")

    print(graph)
    print(schedule)

