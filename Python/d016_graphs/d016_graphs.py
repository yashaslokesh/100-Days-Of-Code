

class Graph:

    def __init__(self):
        self.graph = {}

    def addLink(self, start, end, weight):
        if start in self.graph:
            self.graph[start].append((end, weight))
        else:
            self.graph[start] = [(end, weight)]
        return self

    def __str__(self):
        result = ""
        for node in self.graph:
            result += f"{node} : {self.graph[node]}\n"
        return result

test_graph = Graph()
test_graph.addLink("A","B", 3).addLink("B","C", 4).addLink("C", "E", 5).addLink("D", "E", 4).addLink("A","D", 2)
test_graph.addLink("B","A", 4).addLink("E", "B", 4)

print(test_graph)
