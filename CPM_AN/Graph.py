from FileOperations import getNodesFromFile, getConnectionsFromfile
from Node import Node
from typing import List


def strToNode(name, list_of_nodes):
    return next(node for node in list_of_nodes if node.task == name)


class Graph:
    def __init__(self):
        self.__nodes: List[Node] = []
        self.__CPL = 0
        self.__critical_path = []

    def get_nodes(self):
        return self.__nodes

    def set_nodes(self, fileNameNodes: str, fileNameConnections: str):
        nodes = getNodesFromFile(fileNameNodes)
        connections = getConnectionsFromfile(fileNameConnections)
        if not (nodes or connections):
            raise RuntimeError("Prosze podać pliki z danymi!")
        self.__setPredecessorsAndSuccessors(nodes, connections)
        self.__nodes = nodes
        self.__setAllNodesTags()
        self.__setCPL()
        self.__setAllNodesLs()
        self.__setCriticalPath()

    @property
    def __endpoints(self):
        return [node for node in self.__nodes if not node.successors]

    @property
    def __start_points(self):
        return [node for node in self.__nodes if not node.predecessors]

    @property
    def critical_path(self):
        return self.__critical_path

    @critical_path.setter
    def critical_path(self, value):
        self.__critical_path = value

    def __setPredecessorsAndSuccessors(self, nodes: List[Node], connections):
        # relation example: [A,B]
        for relation in connections:
            for node in nodes:
                if node.task == relation[1]:
                    node.predecessors = strToNode(relation[0], nodes)
                if node.task == relation[0]:
                    node.successors = strToNode(relation[1], nodes)

    def __setAllNodesTags(self):
        self.__setStartingNodesTags()
        not_calculated = [node for node in self.__nodes if node.tag is None]
        calculated = [node for node in self.__nodes if node.tag is not None]

        # iterate to the point when not_calculated is empty
        while not_calculated:
            is_cycle = True
            for node in not_calculated:
                if node.checkIfPredecessorsTagsAreCalculated():
                    node.setTag()
                    calculated.append(node)
                    not_calculated.remove(node)
                    is_cycle = False
            if is_cycle is True:
                raise RuntimeError('Podane dane wskazują, '
                                   'że graf posiada zależności cykliczne')

    def __setStartingNodesTags(self):
        for node in self.__nodes:
            node.setStartingNodeTag()

    def __setCPL(self):
        cpl = None
        for endpoint in self.__endpoints:
            value = endpoint.tag + int(endpoint.duration)
            if cpl is None:
                cpl = value
            elif value > cpl:
                cpl = value
        self.__CPL = cpl

    def __setAllNodesLs(self):
        self.__setEndingNodesLs()
        not_calculated = [node for node in self.__nodes if node.ls is None]
        calculated = self.__endpoints

        # iterate to the point where not_calculated is empty
        while not_calculated:
            for node in not_calculated:
                if node.checkIfSuccessorsLsAreCalculated():
                    node.setLs()
                    calculated.append(node)
                    not_calculated.remove(node)

    def __setEndingNodesLs(self):
        for node in self.__endpoints:
            node.ls = self.__CPL - int(node.duration)

    def __setCriticalPath(self):
        for node in self.__nodes:
            if node.ls == 0:
                self.critical_path.append(node)
        critical_node: Node = self.__critical_path[0]
        while critical_node.successors:
            for node in critical_node.successors:
                if node.tag == node.ls and (node not in self.__critical_path):
                    self.critical_path.append(node)
                    critical_node = node

    def __str__(self):
        nodes = [str(node) for node in self.__nodes]
        critical_nodes = [node.task for node in self.__critical_path]
        critical_path_str = "\nŚcieżka krytyczna: " + " => ".join(critical_nodes)
        nodes_info = '\n'.join(nodes)
        critical_path_time = f"\nDługość ścieżki krytycznej: {self.__CPL} jednostek czasu"
        return nodes_info + critical_path_str + critical_path_time
