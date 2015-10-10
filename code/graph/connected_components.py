# Finding connected components of a simple graph.

# Do a graph traversal to find all connected components.
def compute_ccs(g):
  assert hasattr(g, "vertices")
  assert hasattr(g, "succs")  

  ccs = []                       # connected components
  unvisited = set(g.vertices)    # vertices that have yet to be visited
  frontier = []                  # vertices that belong to current component
  while unvisited:
    cc = set()                   # start visiting a new component
    v = unvisited.pop()
    frontier.append(v)
    unvisited.add(v)             # we actually have yet to visit v
    while frontier:
      v = frontier.pop()
      if v in unvisited:
        # v belongs to the current component
        cc.add(v)
        unvisited.remove(v)
        for u in g.succs[v]:
          frontier.append(u)
    ccs.append(cc)
  return ccs