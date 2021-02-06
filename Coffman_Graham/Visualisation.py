from typing import List
import networkx as nx
import matplotlib.pyplot as plt

from FileOperations import getConnectionsFromFile
from Graph import Graph


def drawGraph(graph: Graph, fileNameConnections: str):
    G = nx.DiGraph()
    G.add_nodes_from(graph.get_nodes())

    edges = getEdgesFromFile(fileNameConnections, graph)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=graph.get_nodes(), alpha=0.7, node_color="b")
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=edges,
        width=2,
        alpha=0.8,
        edge_color="black",
    )

    labels = {n: n.task for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=9)
    plt.axis("on")
    # plt.annotate(str(graph), xy=(-0.16, 0.2), xycoords='axes fraction',
    #              fontsize=10)
    plt.tight_layout()
    plt.show()


def getEdgesFromFile(fileNameConnections: str, graph: Graph):
    edges = getConnectionsFromFile(fileNameConnections)
    for node in graph.get_nodes():
        for sublist in edges:
            for idx, elem in enumerate(sublist):
                if node.task == elem:
                    sublist[idx] = node
    return edges
