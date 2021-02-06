import itertools
from typing import List

from FileOperations import getConnectionsFromFile
from Node import Node


def flatten(list2d):
    return list(itertools.chain(*list2d))


def uniqueList(list_of_nodes):
    return list(set(list_of_nodes))


def nodeWithLexicographicMinTask(nodes_set: List[Node]):
    if not nodes_set:
        raise RuntimeError('Podane dane wskazują, '
                           'że graf posiada zależności cykliczne')
    min_s_list_node = None
    for node in nodes_set:
        if min_s_list_node is None:
            min_s_list_node = node
        elif node.s_list < min_s_list_node.s_list:
            min_s_list_node = node
    return min_s_list_node


def getListOfNodesWithoutTagButReadyToGetOne(list_of_nodes):
    result = []
    for node in list_of_nodes:
        if (node.tag is None) and node.checkIfSuccessorsHaveTags():
            result.append(node)
    return result


class Graph:
    def __init__(self):
        self.__nodes: List[Node] = []

    # get nodes sorted by tag
    def get_nodes(self):
        return self.__nodes

    def set_nodes(self, fileNameConnections: str):
        connections = getConnectionsFromFile(fileNameConnections)
        self.__addNodes(connections)
        self.__setPredecessorsAndSuccessors(connections)
        self.__assignNumbersToS_Lists()
        self.__nodes.sort(key=lambda x: x.tag)

    def __addNodes(self, connections):
        self.__nodes = [Node(strNode) for strNode in uniqueList(flatten(connections))]

    # connections = [['A', 'B'], ['B', 'D'], ['B', 'E'], ['C', 'B'], ['D', 'F'], ['E', 'D'], ['E', 'F']]
    def __setPredecessorsAndSuccessors(self, connections):
        # relation[0] - predecessor to relation[1]
        # relation[1] - successor to relation[0]
        for relation in connections:
            for node in self.__nodes:
                if node.task == relation[0]:
                    node.successors = self.__getNodeFromNodesList(relation[1])
                if node.task == relation[1]:
                    node.predecessors = self.__getNodeFromNodesList(relation[0])

    def __getNodeFromNodesList(self, task):
        return next(node for node in self.__nodes if node.task == task)

    def __assignNumbersToS_Lists(self):
        n = len(self.__nodes)
        for i in range(1, n+1):
            nodes_without_tag_but_ready = getListOfNodesWithoutTagButReadyToGetOne(self.__nodes)
            for node in nodes_without_tag_but_ready:
                if not node.s_list:
                    node.completeS_List()
            nodeWithLexicographicMinTask(nodes_without_tag_but_ready).tag = i

    def __str__(self):
        nodes = [str(node) for node in self.__nodes]
        return '\n'.join(nodes)
