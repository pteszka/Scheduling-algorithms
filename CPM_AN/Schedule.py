from typing import List
from tabulate import tabulate

from Graph import Graph
from Node import Node


class Machines:
    def __init__(self, graph: Graph):
        self.__graph_machine = graph

    @property
    def graph_machine(self):
        return self.__graph_machine

    @graph_machine.setter
    def graph_machine(self, value):
        self.__graph_machine = value

    def __filledFirstColumn(self, critical_path_List: List[Node]):
        column = []
        numbers_of_rows = 0
        for node in critical_path_List:
            name = str(node).split(":")[0]
            for i in range(int(node.duration)):
                column.append([name])
                numbers_of_rows += 1
        return column, numbers_of_rows

    def __makeTabel(self, num_of_rows: int):
        schedule: List[Node] = self.graph_machine.critical_path
        not_in_schedule: List[Node] = [node for node in self.graph_machine.get_nodes() if node not in self.graph_machine.critical_path]
        table_of_tables = []
        while not_in_schedule:
            for node in not_in_schedule:
                # check if schedule contains all elems of node.predecessors
                if all(elem in schedule for elem in node.predecessors):
                    max_tag = 0
                    for parent_node in node.predecessors:
                        if parent_node.tag > max_tag:
                            max_tag = parent_node.tag + int(parent_node.duration)
                    table = ['-'] * num_of_rows
                    name = str(node).split(":")[0]
                    for d in range(int(node.duration)):
                        table[max_tag+d] = name

                    table_of_tables.append(table)
                    schedule.append(node)
                    not_in_schedule.remove(node)

        return table_of_tables

    def __str__(self):
        table, num_of_rows = self.__filledFirstColumn(self.graph_machine.critical_path)
        rest_columns = self.__makeTabel(num_of_rows)
        for rest_column in rest_columns:
            for idx, entity in enumerate(rest_column):
                table[idx].append(entity)
        headers = [f"M{i}"for i in range(len(table))]
        return tabulate(table, headers=headers, tablefmt="grid")
