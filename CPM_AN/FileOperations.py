from Node import Node


def readLinesFromFile(fileNameNodes):
    file_path = f"Data/{fileNameNodes}"
    with open(file_path) as f:
        content = f.readlines()
    return content


def getNodesFromFile(fileNameNodes: str):
    content = readLinesFromFile(fileNameNodes)
    # X,Y\n -> list(X,Y)
    content = [e.strip().split(",") for e in content if not e.isspace()]
    return [Node(e[0], e[1]) for e in content]


def getConnectionsFromfile(fileNameConnections: str):
    content = readLinesFromFile(fileNameConnections)
    # (X,Y)\n -> list(X,Y)
    return [e.rstrip().strip("( )").split(",") for e in content if not e.isspace()]


