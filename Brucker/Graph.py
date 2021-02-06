import itertools

from FileOperations import getNodesFromFile, getConnectionsAndMachinesFromFile
from Node import Node
from typing import List


def strToNode(name, list_of_nodes):
    return next(node for node in list_of_nodes if node.task == name)


def flatten(list2d):
    return list(itertools.chain(*list2d))


class Graph:
    def __init__(self):
        self.__nodes: List[Node] = []
        self.__machines = 0

    @property
    def machines(self):
        return self.__machines

    @machines.setter
    def machines(self, value):
        self.__machines = value

    def get_nodes(self):
        return self.__nodes

    def set_nodes(self, fileNameNodes: str, fileNameConnections: str):
        nodes = getNodesFromFile(fileNameNodes)
        connections, machines = getConnectionsAndMachinesFromFile(fileNameConnections)
        if not (nodes or connections):
            raise RuntimeError("Prosze podać pliki z danymi!")
        self.__machines = machines
        self.__setPredecessorsAndSuccessors(nodes, connections)
        self.__nodes = nodes
        self.__setNodesTags()

    def __setPredecessorsAndSuccessors(self, nodes: List[Node], connections):
        # relation example: [A,B]
        for relation in connections:
            for node in nodes:
                if node.task == relation[1]:
                    node.predecessors = strToNode(relation[0], nodes)
                if node.task == relation[0]:
                    node.successor = strToNode(relation[1], nodes)

    def __setNodesTags(self):
        self.__setRootTag()
        list_of_remaining_ones = self.__setRootTag().predecessors

        # while list_of_remaining_ones is not empty
        while list_of_remaining_ones:
            for node in list_of_remaining_ones:
                if node.successor.tag is None:
                    raise RuntimeError('Podane dane wskazują, '
                                       'że graf posiada zależności cykliczne')
                node.tag = max(1 + node.successor.tag, 1 - node.duration)
            # Add predecessors of nodes only if they exists.
            # Then flatten list in case if any node has more than 1 predecessor
            list_of_remaining_ones = flatten([node.predecessors for node in list_of_remaining_ones if node is not None])

    def __setRootTag(self):
        is_tree_intree = 0
        root = None
        for node in self.__nodes:
            if node.successor is None:
                node.tag = 1 - node.duration
                root = node
                is_tree_intree += 1
        if is_tree_intree > 1:
            raise Exception("Podane drzewo nie jest intree!")

        return root

    def __str__(self):
        nodes = [str(node) for node in self.__nodes]
        nodes_info = '\n'.join(nodes)
        return nodes_info
