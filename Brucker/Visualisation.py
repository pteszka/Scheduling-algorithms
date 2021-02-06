import plotly.graph_objects as go
from plotly.graph_objs import Scatter, Layout
from igraph import Graph, EdgeSeq
from Graph import Graph as BruckerGraph
import plotly

# plotly.offline.plot({
#     "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": Layout(title="hello world")
# })
from FileOperations import getConnectionsAndMachinesFromFile, getNodesFromFile


def drawGraph(graph: BruckerGraph, fileNameConnections: str):
    plotly.offline.plot(setUpTree(graph, fileNameConnections))


def setUpTree(graph: BruckerGraph, fileNameConnections: str):
    edges, _ = getConnectionsAndMachinesFromFile(fileNameConnections)
    edges = listOfListsToListOfTuples(edges)
    nodes = graph.get_nodes()

    nr_vertices = len(nodes)
    v_label = list(map(str, range(nr_vertices)))
    G = Graph.Tree(nr_vertices, 2)  # 2 stands for children number
    lay = G.layout('rt')

    position = {k: lay[k] for k in range(nr_vertices)}
    Y = [lay[k][1] for k in range(nr_vertices)]
    M = max(Y)

    es = EdgeSeq(G)  # sequence of edges
    E = [e.tuple for e in G.es]  # list of edges

    L = len(position)
    Xn = [position[k][0] for k in range(L)]
    Yn = [2 * M - position[k][1] for k in range(L)]
    Xe = []
    Ye = []
    for edge in E:
        Xe += [position[edge[0]][0], position[edge[1]][0], None]
        Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]
    labels = v_label

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Xe,
                       y=Ye,
                       mode='lines',
                       line=dict(color='rgb(210,210,210)', width=1),
                       hoverinfo='none'
                       ))
    fig.add_trace(go.Scatter(x=Xn,
                      y=Yn,
                      mode='markers',
                      name='bla',
                      marker=dict(symbol='circle-dot',
                                    size=18,
                                    color='#6175c1',    #'#DB4551',
                                    line=dict(color='rgb(50,50,50)', width=1)
                                    ),
                      text=labels,
                      hoverinfo='text',
                      opacity=0.8
                      ))
    return fig

def createTextInsideCircles():
    pass


def listOfListsToListOfTuples(list_of_lists):
    return [tuple(entity) for entity in list_of_lists]
