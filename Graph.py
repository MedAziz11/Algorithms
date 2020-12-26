from Node import Node


class Graph(object):

    def __populateGraph(self, adj_list):
        self.graph = {}
        for key, neighbors in adj_list.items():
            self.addNode(Node(key, neighbors))

        return self.graph

    def __init__(self, adj_list=None):
        self.graph = self.__populateGraph(adj_list) if adj_list else {}

    def addNode(self, node: Node):
        """add a new Node"""
        self.graph[node.key] = node

    def addEdge(self, from_n1: Node, to_n2: Node, cost: int) -> Node:
        """add a new Edge between 2 existant nodes"""

        if from_n1 not in self.graph:
            self.addNode(Node(from_n1))
        if to_n2 not in self.graph:
            self.addNode(Node(to_n2))
        self.graph[from_n1].addNeighbor(self.verticies[to_n2], cost)

        return self.graph[from_n1]

    def removeEdge(self, n1 ,n2) -> Node:
        """remove an Edge between 2 existant nodes"""
        self.graph[n1].removeNeighbor(n2)
        return self.graph[n1]

    def getConnections(self, n1):
        """get all directed connection to a specific Node"""
        return [key for key, vals in self.graph.items() if n1 in vals]

    def popNode(self, n_key):
        """pop an existing Node from the graph"""
        for key in self.getConnections(n_key):
            self.removeEdge(key, n_key)

        self.graph.pop(n_key)
    
    def __call__(self):
        for key in self.graph:
            print(self.graph[key])

    def __len__(self):
        return len(self.graph)

    def __iter__(self):
        return (iter(self.graph.keys()))
    
    def __getitem__(self, key):
        return self.graph[key]

    def __contains__(self, node):
        return node in self.graph

    def __repr__(self):
        return f"<Graph({self.nodes})>"


if __name__ == "__main__":
    adj_list = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }
    graph = Graph(adj_list)
    print(graph.getConnections("Z"))
    graph.popNode('Z')
    graph()