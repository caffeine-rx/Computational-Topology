# An implementation of the find-union data structure for simple graphs.

# Simple find-union without path compression.
class NaivePartition(object):
      
  def __init__(self, graph):
    assert hasattr(graph, 'edges')
    assert hasattr(graph, 'vertices')
    self.parent = dict((v, None) for v in graph.vertices)
    for u, v in graph.edges:
      self.union(u, v)

  def find(self, v):
    if self.parent[v] is None:
      return v
    else:
      return self.find(self.parent[v])
  
  def union(self, u, v):
    x = self.find(u)
    y = self.find(v)
    if x != y:
      self.parent[x] = y

# Find-union with path compression. This algorithm can
# be improved by assigning integer ids to all vertices
# and make self.parent an array (list).
class Partition(NaivePartition):
  
  __init__ = NaivePartition.__init__
  
  def find(self, v):
    parent = self.parent[v]
    if parent is None:
      parent = v
    else:
      parent = self.parent[v] = self.find(parent)
    return parent