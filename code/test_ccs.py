from graph import connected_components as ccmod
from graph import simple_graph as sg
from graph import partition as part
from graph import load

from timer import Timer
import sys
sys.setrecursionlimit(10000) # NaivePartition needs this

# Compute the connected components of graph g.
def compute_ccs(g, Partition):
  p = Partition(g)
  ccs = dict()
  for v in g.vertices:
    c = p.find(v)
    if c not in ccs:
      ccs[c] = set()
    ccs[c].add(v)
  return ccs

vs, es = load.load_snap_undirected('data/snap/ca-GrQc.txt')
g = sg.SimpleGraph(vs, es)
n = len(g.vertices)
m = len(g.edges)
print("Loaded graph with %d vertices and %d edges" % (n, m))
print()

print("Computing connected components with naive find-union:")
with Timer(verbose=True):
    ccs = compute_ccs(g, part.NaivePartition)
    print("found %d components" % len(ccs))

print()
print("Computing connected components with efficient find-union:")
with Timer(verbose=True):
    ccs = compute_ccs(g, part.Partition)
    print("found %d components" % len(ccs))

print()
print("Computing connected components with graph traversal:")
with Timer(verbose=True):
    ccs = ccmod.compute_ccs(g)
    print("found %d components" % len(ccs))
