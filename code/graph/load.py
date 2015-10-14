# This code loads graphs from the data directory.

# Load a graph from the SNAP collection, assuming it is an undirected graph.
def load_snap_undirected(filepath):
  vertices = set()
  edges = set()
  for line in open(filepath):
    if line[0] == '#':
      continue # skip header
      # Each line contains two node ids separated by a tab.
    line = line.strip()
    u, v = line.split('\t')
    vertices.add(u)
    vertices.add(v)
    edges.add((u,v))
  return vertices, edges
