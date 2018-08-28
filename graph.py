### Graph ####

class Node:
  def __init__(self, node):
    self.node = node
    self.edges = []

class Edge:
  def __init__(self, node_from, node_to, weight):
    self.node_from = node_from
    self.node_to = node_to
    self.weight = weight


class Graph:
  def __init__(self, nodes= [], edges = []):
    self.nodes = nodes
    self.edges = edges

  def insert_node(self, new_node):
    if Node(new_node) not in self.nodes:
      self.nodes.append(Node(new_node))

  def insert_edge(self, new_from, new_to, new_weight):
    from_found = None
    to_found = None
    for n in self.nodes:
      if n.node == new_from:
        from_found = n
      if n.node == new_to:
        to_found = n
    if from_found == None:
      self.nodes.append(Node(new_from))
      from_found = Node(new_from)
    if to_found == None:
      self.nodes.append(Node(new_to))
      to_found = Node(new_to)
    from_found.edges.append(Edge(new_from, new_to, new_weight))
    to_found.edges.append(Edge(new_from, new_to, new_weight))
    self.edges.append(Edge(new_from, new_to, new_weight))

  def get_edge_list(self):
    res = []
    for edge in self.edges:
        res.append((edge.node_from, edge.node_to, edge.weight))
    return res

  def get_node_list(self):
    res = []
    for n in self.nodes:
      res.append(n.node)
    return res

  def get_adjacency_list(self):
    res = []
    for n in self.nodes:
        adj = []
        flag = 0
        for edge in n.edges:
            if edge.node_from == n.node:
                adj.append((edge.node_to, edge.weight))
                flag = 1
        if flag == 0:
            res.append(None)
        else:
            res.append(adj)
    return res

  def get_adjacency_matrix(self):
    res = []
    for i in range(len(self.nodes)):
      adj = [0]*len(self.nodes)
      for edge in self.nodes[i].edges:
        if edge.node_from == self.nodes[i].node:
          adj[self.get_node_list().index(edge.node_to)] = edge.weight
      res.append(adj)
    return res


  

graph = Graph()
graph.insert_node('1')
graph.insert_node('3')
graph.insert_node('2')
graph.insert_edge('2', '1', 100)
graph.insert_edge('2', '3', 200)
graph.insert_edge('1', '3', 300)

print(graph.get_edge_list())

graph.insert_edge('1', '7', 350)
graph.insert_edge('1', '5', 400)
print(graph.get_edge_list())

print(graph.get_node_list())
print(graph.get_adjacency_list())
print graph.get_adjacency_matrix()
