# Kruskal's algorithm in Python


class graph:
    def __init__(self, ver):
        self.V = ver
        self.graph = []

    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])

    # Search function

    def find(self, origin, i):
        if origin[i] == i:
            return i
        return self.find(origin, origin[i])

    def apply_union(self, origin, status, x, y):
        xpath = self.find(origin, x)
        ypath = self.find(origin, y)
        if status[xpath] < status[ypath]:
            origin[xpath] = ypath
        elif status[xpath] > status[ypath]:
            origin[ypath] = xpath
        else:
            origin[ypath] = xpath
            status[xpath] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, j = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        origin = []
        status = []
        for node in range(self.V):
            origin.append(node)
            status.append(0)
        while j < self.V - 1:
            a, b, c = self.graph[i]
            i = i + 1
            x = self.find(origin, a)
            y = self.find(origin, b)
            if x != y:
                j = j + 1
                result.append([a, b, c])
                self.apply_union(origin, status, x, y)
        for a, b, weight in result:
            print("%d - %d: %d" % (a, b, weight))


g = Graph(6)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()