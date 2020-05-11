class Graph:
  def __init__(self):
    self.verticies = {}


  def add_node(self,node):
    self.verticies[node] = []


  def add_edge(self,node_a,node_b):
    self.verticies[node_a].append(node_b)
    self.verticies[node_b].append(node_a)

  def subgraph(self, start):

    items = set()
    self._dfs(start, items)
    return items

  def _dfs(self, start, items):

    if start not in items:
      items.add(start)
      adj = self.verticies[start]
      for node in adj:
        self._dfs(node,items)


graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('Z')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('D', 'B')

print(graph.subgraph('A'))
