#EXAMPLE OF HOW *NOT* TO WRITE THE CODE FOR GRAPH CONNECTEDNESS!
#As I wrote this, I discovered how using a class for vertices just added a bunch of useless structure - not only that, but I discovered you can't pass objects by reference making the whole thing too cumbersome to be useful.  I'm now writing the code for this assignment without using classes.

#Mike Wells,  MTH610,  Union-Find program

#vertices: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#edges: (1,2) (2,3) (2,4), (3,2), (4,2)
#edges: (5,6), (5,7), (5,8), (6,5), (7,5) (8,5), (9, 10), (10, 9)

edges_1 = [2]
edges_2 = [3,4]
edges_3 = [2]
edges_4 = [2]
edges_5 = [6,7,8]
edges_6 = [5]
edges_7 = [5]
edges_8 = [5]
edges_9 = [10]
edges_10 = [9]

class Vertex:
	def __init__(self, number, edges = [], *args):
		self.edges = edges
		self.parent = number
		self.number = number
	def set_parent(self, parent):
		self.parent = parent	

Node = [Vertex(1,edges_1), Vertex(2,edges_2), Vertex(3,edges_3), Vertex(4,edges_4), Vertex(5,edges_5), Vertex,(6,edges_6), Vertex(7,edges_7), Vertex(8,edges_8), Vertex(9, edges_9), Vertex(10,edges_10)]

def Find(v = Vertex):
	if(v.parent == v.number):
		return v.number
	else:
		j = v.parent
		Find(Node[j])

def Union(i,j, Node = [], *arg):
	x1 = Find(Node[i])
	x2 = Find(Node[j])
	if(x1 != x2):
		Node[x2].parent = (Node[x1].number - 1)
	else:
		return
Union(0,1, Node)
print Node[0].parent
print Node[1].parent
