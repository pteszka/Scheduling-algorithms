from Graph import Graph as BruckerGraph
from Schedule import Schedule

# Press the green button in the gutter to run the script.
from Visualisation import drawGraph

if __name__ == '__main__':
    graph = BruckerGraph()
    graph.set_nodes("NodesA", "GraphA")
    schedule = Schedule(graph)
    schedule.print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
