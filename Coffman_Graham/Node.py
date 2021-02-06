from typing import List


class Node:
    def __init__(self, task):
        self.__task = task
        self.__tag = None
        self.__s_list: List[int] = []
        self.__predecessors: List[Node] = []
        self.__successors: List[Node] = []

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        self.__task = value

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        self.__tag = value

    # we always get s_list sorted decreasing
    @property
    def s_list(self):
        return sorted(self.__s_list, reverse=True)

    @s_list.setter
    def s_list(self, value):
        self.__s_list.append(value)

    @property
    def predecessors(self):
        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value):
        self.__predecessors.append(value)

    @property
    def successors(self):
        return self.__successors

    @successors.setter
    def successors(self, value):
        self.__successors.append(value)

    def checkIfSuccessorsHaveTags(self):
        for successor in self.successors:
            if successor.tag is None:
                return False
        return True

    def completeS_List(self):
        for node in self.successors:
            self.s_list = node.tag

    def __str__(self):
        return f"{self.task}, {self.tag}: {[str(num) for num in self.s_list]}"
