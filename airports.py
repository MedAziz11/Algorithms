class Graph(object):

    def __populateGraph(self, airports, routes):
        self.graph = {airport : [] for airport in airports}
        for route in routes:
            self.addEdge(*route)

        return self.graph

    def __init__(self, airports, routes):
        self.graph = self.__populateGraph(airports, routes)


    def addNode(self, node):
        self.graph[node] = []

    def addEdge(self, origin, destination):
        self.graph[origin].append(destination)
        self.graph[destination].append(origin)

    def DFS(self, start, finish, visited= set()):
    #DFS Depth-First-Search
        visited.add(start)
        dests = self.graph[start]

        for dest in dests:

            if (dest==finish):
                print('Found')
                return

            if not(dest in visited):
                self.DFS(dest, finish, visited)



if __name__ == "__main__":

    airports = "PHX BKK OKC JFK MEX".split()
    routes = [
        ["PHX", "BKK"],
        ["PHX", "OKC"],
        ["BKK", "JFK"],
        ["OKC", "MEX"],
        ["JFK", "MEX"],
    ]

    g= Graph(airports, routes)
    print(g.graph)
    g.DFS('PHX', 'MEX')