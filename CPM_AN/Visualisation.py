from typing import List
import networkx as nx
import matplotlib.pyplot as plt

from FileOperations import getConnectionsFromfile
from Graph import Graph


def drawGraph(graph: Graph, fileNameConnections: str):
    G = nx.DiGraph()
    G.add_nodes_from(graph.get_nodes())

    edges = getEdgesFromFile(fileNameConnections, graph)
    critical_path, edges = getCriticalAndNonPathEdgesFromEdges(graph, edges)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=graph.get_nodes(), alpha=0.7, node_color="b")
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=critical_path,
        width=2,
        alpha=0.8,
        edge_color="red",
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=edges,
        width=2,
        alpha=0.8,
        edge_color="black",
    )
    # G = nx.relabel_nodes(G, mapping(graph))

    labels = {n: n.task for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=9)
    plt.axis("off")
    plt.show()


def getEdgesFromFile(fileNameConnections: str, graph: Graph):
    edges = getConnectionsFromfile(fileNameConnections)
    for node in graph.get_nodes():
        for sublist in edges:
            for idx, elem in enumerate(sublist):
                if node.task == elem:
                    sublist[idx] = node
    return edges


def getCriticalAndNonPathEdgesFromEdges(graph: Graph, edges: List):
    critical_path_nodes = graph.critical_path
    # edge = [A,B]
    critical_path = []
    for edge in edges:
        # is edge part of critical path?
        if set(edge).issubset(set(critical_path_nodes)):
            critical_path.append(edge)
            edges.remove(edge)
    return critical_path, edges
