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


def getConnectionsAndMachinesFromFile(fileNameConnections: str):
    content = readLinesFromFile(fileNameConnections)
    connections = []
    machines = 0
    for line in content:
        if not line.isspace():
            try:
                line = int(line.rstrip())
                machines = line
            except ValueError:
                connections.append(line.rstrip().strip("( )").split(","))
    return connections, machines

