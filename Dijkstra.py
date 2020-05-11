class Node():

    def __init__(self, key):

        self.key = key
        self.neighbors = []

    def __repr__(self):

        return ("Node", self.key, self.neighbors)

class Graph():

    def __init__(self, nodes, edges):

        """
        nodes: array of keys
        edges: array of tuples in format (start,end,weight)
        """

        self.nodes = {}
        for node in nodes:
            self.nodes[node] = Node(node)

        for edge in edges:

            start,end,weight = edge
            self.nodes[start].neighbors.append((end,weight))

    def __repr__(self):

        to_return = ""

        for node in self.nodes:
            to_add = self.nodes[node].__repr__()
            to_return += str(to_add) + "\n"

        return to_return

    def dijkstra(self,start):
        pass

nodes = ["A","B","C","D","E","F"]
edges = [
        ("A","B",7),("A","C",9),("A","E",14),
        ("B","C",10),("B","D",15),
        ("C","D",11),("C","E",2),
        ("D","F",6),("E","F",9)
        ]

graph = Graph(nodes,edges)
print(graph)
