from Node import Node


def readLinesFromFile(fileNameNodes):
    file_path = f"Data/{fileNameNodes}"
    with open(file_path) as f:
        content = f.readlines()
    return content


def getConnectionsFromFile(fileConnections: str):
    # [(X,Y)\n, ,(A,Y)\n ...] -> [[X,Y],[A,Y]...]
    content = readLinesFromFile(fileConnections)
    connections = []
    for data in content:
        if not data.isspace():
            connections.append(data.rstrip().strip("( )").split(","))
    return connections
