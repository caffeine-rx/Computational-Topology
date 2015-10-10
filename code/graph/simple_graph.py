# A data structure for representing simple, undirected graphs.

class SimpleGraph(object):
  
  def __init__(self, vertices, edges):
    self.vertices = frozenset(vertices)
    self.edges = frozenset(edges)

    # Create incidences used by some algorithms.
    succs = dict((v, set()) for v in vertices)
    for i, j in edges:
      assert i in vertices
      assert j in vertices
      succs[i].add(j)
      succs[j].add(i)
    self.succs = succs
