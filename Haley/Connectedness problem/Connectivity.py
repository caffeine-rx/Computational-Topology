# Haley Bourke
# Connectedness decidability problem (union-find algorithm)

class Connectivity(object):

    def __init__(self, parent, edges):
        self.parent = parent;
        self.edges = edges;

    def Find(self, v):
        if(self.parent[v] == v): # if the vertex has no parent, that means it is the root
            return v;        # so we return the vertex

        return self.Find(self.parent[v]); # recurse until we find the root

    def Union(self, vertex1, vertex2):
        root1 = self.Find(vertex1); # recursively find the root of the first vertex
        root2 = self.Find(vertex2);

        if(root1 == root2): # if the roots of vertex 1 & 2 are the same...
            return; # we're done (they're a part of the same component)

        self.parent[vertex2] = vertex1; # otherwise we "union" the components
        return;

    # I think I envisioned this a bit differently than my classmates
    # instead of hardcoding graph or generating one randomly, 
    # I assumed that the user would give the graph and the library functions
    # would return whether the user-specified graph is connected or     not
    # the graph should be specified by a list of vertices as an array which holds the
    # parent index of the index
    # and an array of 2-tuples specifying the edges
    def isConnected(self):
        for (index1, index2) in self.edges: # iterate through the given edges
            self.Union(index1, index2); # and union them as we go
        
            numRoots = 0;
    
        for x in range(0, len(self.parent) - 1):
                if(self.parent[x] == x):
                    numRoots = numRoots + 1;
    
        if(numRoots == 1):
                return "true";
        else:
                return "false";


