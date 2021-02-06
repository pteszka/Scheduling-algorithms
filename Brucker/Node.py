from typing import List


class Node:
    def __init__(self, task, duration):
        self.__task = task
        self.__duration = duration
        self.__tag = None
        self.__predecessors: List[Node] = []
        self.__successor = None
        self.__c = None
        self.__on_machine = False
        self.__L = None

    @property
    def L(self):
        return self.__L

    @L.setter
    def L(self, value):
        self.__L = value

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        self.__task = value

    @property
    def duration(self):
        return int(self.__duration)

    @duration.setter
    def duration(self, value):
        self.__duration = int(value)

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        self.__tag = value

    @property
    def predecessors(self):
        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value):
        self.__predecessors.append(value)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        self.__successor = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    @property
    def on_machine(self):
        return self.__on_machine

    @on_machine.setter
    def on_machine(self, value):
        self.__on_machine = value

    # def AllPredecessorsAreOnMachines(self):
    #     return all([ancestor.c is not None for ancestor in self.predecessors])

    def __str__(self):
        return f"{self.task}({self.duration}), tag: {self.tag}, c:{self.c}, l:{self.L}"
