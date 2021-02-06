from typing import List


class Node:
    def __init__(self, task, duration):
        self.__task = task
        self.__duration = duration
        self.__tag = None  # earliest start
        self.__ls = None  # latest start
        self.__predecessors: List[Node] = []
        self.__successors: List[Node] = []

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        self.__task = value

    @property
    def duration(self):
        return self.__duration

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
    def ls(self):
        return self.__ls

    @ls.setter
    def ls(self, value):
        self.__ls= value

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

    def checkIfPredecessorsTagsAreCalculated(self):
        for predecessor in self.__predecessors:
            if predecessor.__tag is None:
                return False
        return True

    def setTag(self):
        max_tag = None
        for predecessor in self.__predecessors:
            value = predecessor.__tag + int(predecessor.__duration)
            if max_tag is None:
                max_tag = value
            elif value > max_tag:
                max_tag = value
        self.__tag = max_tag

    def checkIfSuccessorsLsAreCalculated(self):
        for successor in self.__successors:
            if successor.__ls is None:
                return False
        return True

    def setLs(self):
        min_ls = None
        for successor in self.__successors:
            value = successor.__ls - int(self.__duration)
            if min_ls is None:
                min_ls = value
            elif value < min_ls:
                min_ls = value
        self.__ls = min_ls

    def setStartingNodeTag(self):
        if not self.__predecessors:
            self.__tag = 0

    def __str__(self):
        return f"{self.task}: ES - {self.tag}, LS - {self.ls}"