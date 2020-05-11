class SocialGraph:
  def __init__(self):
    self.members = {}


  def add_node(self,node):
    self.members[node] = set()


  def add_edge(self,node_a,node_b):
    self.members[node_a].add(node_b)
    self.members[node_b].add(node_a)

  def subgraph(self, root):
    to_visit = [root]

    visited = set()

    while len(to_visit) > 0:
      node = to_visit.pop(0)
      if node not in visited:

        visited.add(node)

        for neighbor in self.members[node]:
          to_visit.append(neighbor)
    return visited

  def suggest_friends(self, me):

    friends_score = {}

    adj = self.members[me]

    for friend in adj:

        friend_adj = self.members[friend]

        for friend_of_friend in friend_adj:

            if friend_of_friend is not me and friend_of_friend not in adj:

                if friend_of_friend in friends_score:
                    friends_score[friend_of_friend] += 1
                else:
                    friends_score[friend_of_friend] = 1

    max = 0
    to_return = set()
    for key in friends_score:

        if max < friends_score[key]:

            to_return = set()
            to_return.add(key)
            max = friends_score[key]

        elif max == friends_score[key]:
            to_return.add(key)

    return to_return



graph = SocialGraph()

## Friend Group 1
graph.add_node('Alice')
graph.add_node('Bob')
graph.add_node('Carol')
graph.add_node('Dave')
graph.add_node('Eve')
graph.add_node('Faythe')
graph.add_node('Grace')

## Friend Group 2
graph.add_node('Zed')
graph.add_node('Xavier')
graph.add_node('Quill')
graph.add_node('Robert')


## Friend Group 3
graph.add_node('Heidi')
graph.add_node('Niaj')
graph.add_node('Ivan')
graph.add_node('Trent')


## Friendships
graph.add_edge('Alice', 'Bob')
graph.add_edge('Alice', 'Carol')
graph.add_edge('Alice', 'Dave')
graph.add_edge('Bob', 'Dave')
graph.add_edge('Carol', 'Dave')
graph.add_edge('Alice', 'Eve')
graph.add_edge('Eve', 'Grace')
graph.add_edge('Eve', 'Bob')
graph.add_edge('Faythe', 'Eve')
graph.add_edge('Dave', 'Faythe')
graph.add_edge('Grace', 'Faythe')


graph.add_edge('Xavier', 'Quill')
graph.add_edge('Robert', 'Quill')
graph.add_edge('Xavier', 'Robert')
graph.add_edge('Zed', 'Quill')
graph.add_edge('Zed', 'Xavier')

graph.add_edge('Heidi', 'Niaj')
graph.add_edge('Heidi', 'Ivan')
graph.add_edge('Heidi', 'Trent')
graph.add_edge('Niaj', 'Trent')
graph.add_edge('Ivan', 'Trent')
graph.add_edge('Niaj', 'Ivan')

print(graph.suggest_friends('Faythe'))
print(graph.suggest_friends('Robert'))
print(graph.suggest_friends('Ivan'))
