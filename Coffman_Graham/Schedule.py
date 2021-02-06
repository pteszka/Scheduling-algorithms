from typing import List

from Graph import Graph
from tabulate import tabulate
import copy


def transposeListOfLists(machines):
    return list(map(list, zip(*machines)))


def getMachinesOfTheSameLen(machines: List[List[str]]):
    if len(machines[0]) > len(machines[1]):
        machines[1].append("X")
    elif len(machines[1]) > len(machines[0]):
        machines[0].append("X")
    return machines


def arePredecessorsOnSchedule(machines, entity):
    for ancestor in entity.predecessors:
        if not any(ancestor.task in sl for sl in machines):
            return False
    return True


def isOnM1AnyPredecessor(machines, entity):
    # check if on last position of M1 is ancestor
    return True if machines[0][-1] in [ancestor.task for ancestor in entity.predecessors] else False


class Schedule:
    def __init__(self, graph: Graph):
        self.__graph_machine = graph

    @property
    def graph_machine(self):
        return self.__graph_machine

    @graph_machine.setter
    def graph_machine(self, value):
        self.__graph_machine = value

    def __getCompleteMachines(self):
        machines = [[], []]
        tasks = copy.deepcopy(list(reversed(self.__graph_machine.get_nodes())))
        # counter changes the machine we are looking at
        counter = 0
        while tasks:
            did_tasks_change = False
            for node in tasks:
                if arePredecessorsOnSchedule(machines, node):
                    if (counter % 2 == 1) and isOnM1AnyPredecessor(machines, node):
                        continue
                    machines[counter % 2].append(node.task)
                    tasks.remove(node)
                    did_tasks_change = True
                    break
            if did_tasks_change is False:
                machines[counter % 2].append("X")
            counter += 1
        getMachinesOfTheSameLen(machines)
        c_max = max([len(machine) for machine in machines])
        return c_max, machines

    def __str__(self):
        headers = ["M1", "M2"]
        c_max, machines = self.__getCompleteMachines()
        transposed_table = transposeListOfLists(machines)
        return tabulate(transposed_table, headers=headers, tablefmt="grid") + f"\nC_max = {c_max}"
