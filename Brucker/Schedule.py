from itertools import repeat
from typing import List

from Graph import Graph
from tabulate import tabulate
from itertools import repeat
import itertools
from Node import Node
import copy


def transposeListOfLists(machines):
    return list(map(list, zip(*machines)))


def listOfListsOfNodesToTasks(machines):
    return [["X" if entity is "X" else entity.task for entity in machine] for machine in machines]


# def getMachinesOfTheSameLen(machines: List[List[str]]):
#     if len(machines[0]) > len(machines[1]):
#         machines[1].append("X")
#     elif len(machines[1]) > len(machines[0]):
#         machines[0].append("X")
#     return machines


def setCofNodesOnSchedule(schedule):
    pass


def flatten(list2d):
    return list(itertools.chain(*list2d))


def getNodeWithMaxTag(list_of_nodes: List[Node]):
    max_val = max(node.tag for node in list_of_nodes)
    return next((node for node in list_of_nodes if node.tag == max_val))


# ta funkcja zmienia wszystkie atrybuty onMachine na True - czemu?
def setNodesReadyToBePlaced(nodes):
    nodes_ready_to_be_placed = []
    for node in nodes:
        arePredecessorsOnMachine = True
        for ancestor in node.predecessors:
            if ancestor.on_machine is False:
                arePredecessorsOnMachine = False

        if arePredecessorsOnMachine is True and node.on_machine is False:
            nodes_ready_to_be_placed.append(node)
    return nodes_ready_to_be_placed


def setC(machines):
    for machine in machines:
        for i, node in enumerate(machine, start=1):
            if node != "X":
                node.c = i


class Schedule:
    def __init__(self, graph: Graph):
        self.__graph_machine = copy.deepcopy(graph)

    @property
    def graph_machine(self):
        return self.__graph_machine

    @graph_machine.setter
    def graph_machine(self, value):
        self.__graph_machine = value

    # wymyśl jak dopełnic pozostale maszyny
    def __getCompleteMachinesAndL_Max(self):
        nodes = self.graph_machine.get_nodes()
        machines = [[] for _ in range(self.__graph_machine.machines)]
        nodes_ready_to_be_placed = [node for node in nodes if not node.predecessors]
        number_of_machines = len(machines)

        while nodes_ready_to_be_placed:
            for machine in range(number_of_machines):
                if nodes_ready_to_be_placed:
                    node_with_max_tag = getNodeWithMaxTag(nodes_ready_to_be_placed)
                    machines[machine].append(node_with_max_tag)
                    node_with_max_tag.on_machine = True
                    nodes_ready_to_be_placed.remove(node_with_max_tag)
                else:
                    machines[machine].append("X")

            nodes_ready_to_be_placed = setNodesReadyToBePlaced(nodes)
        setC(machines)
        l_max = self.__calculateL_Max(machines)
        machines = listOfListsOfNodesToTasks(machines)
        return machines, l_max

    def __calculateL_Max(self, machines):
        l_max = None
        for i, machine in enumerate(machines):
            for node in machine:
                if node == "X":
                    continue
                node.L = node.c - int(node.duration)
                if l_max is None:
                    l_max = 1 - int(node.duration)
                elif (node.c - int(node.duration)) > l_max:
                    l_max = node.c - int(node.duration)
        return l_max

    def print(self):
        headers = [f"M{i + 1}" for i in range(self.__graph_machine.machines)]
        machines, l_max = self.__getCompleteMachinesAndL_Max()
        transposed_table = transposeListOfLists(machines)
        print(tabulate(transposed_table, headers=headers, tablefmt="grid") + f"\nL_max = {l_max}")
        print(self.__graph_machine)

# for i in range(len(machines)):
#     node_with_max_tag = self.getNodeWithMaxTag(nodes_without_predecessor)
#     machines[i].append(node_with_max_tag.task)
#     node_with_max_tag.c = counter
#     completed.append(node_with_max_tag), nodes_without_predecessor.remove(node_with_max_tag)
# # nodes_without_predecessor = Nodes in graph without predecessor - completed
# nodes_without_predecessor = [node for node in nodes if not node.AllPredecessorsAreOnMachines()]
# # nodes_without_predecessor = [x for x in nodes if x not in completed]
# counter += 1
