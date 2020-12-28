class Node(object):
    """Directed Node"""

    def __init__(self, key, neighbors={}):
            self.key = key
            self.neighbors = neighbors#all the succ to a Node
            
    def addNeighbor(self, neighbor, cost=0):
        self.neighbors[neighbor] = cost

    def getNeighbors(self):
        return self.neighbors.keys()

    def removeNeighbor(self, node):
        return  self.neighbors.pop(node)

    def getCost(self, neighbor):
        return self.neighbors[neighbor]

    def __contains__(self, key):
        return key in self.neighbors.keys()

    def __repr__(self):
        return f"<Node {self.key}>"

    def __str__(self):
        return f'{self.key} --> {[node for node in self.neighbors]}'