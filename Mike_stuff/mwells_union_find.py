#Mike Wells  Code for connectedness algorithm for graphs.  10/22/2015 MTH610

#vertex = [1,2,3,4,5,6,7,8,9,10] #Each vertex corresponds to a number 
				#in this list.  
				#***Realized that the list is not needed.***
#The edges are just ordered pairs.  If there is an edge from 1 to 9, the edge
#in this list would be (1,9)
edges = [(1,2),(2,1), (2,3), (2,4), (3,2), (4,2), (5,6), (5,7), (5,8), (6,5), (7,5), (8,5), (9,10), (10,9)]


#Below is a list that keeps track of the vertices' parents.  The first 
#position in the list corresponds to vertex 1 & so we see that the 
#parent of 1 is 1.  For any vertex n, the nth number in the list is 
#vertex n's parent. This will get modified as the program runs so that 
#if two vertices are in the same connected component, one can follow from
#one parent to the next until both paths end at the same vertex, the root.
parent = [1,2,3,4,5,6,7,8,9,10]

def Find(x):
	if (parent[x-1] == x):  #I don't say parent[x] == x since a list
				#of numbers has 0 as its first position.
				#If the parent of a vertex is itself, then
				#that vertex is the root of the current
				#component, which is what this function
				#is looking for.
		return x
	else:
		return Find(parent[x-1]) #if the vertex is not the root,
					 #check to see if its parent is the 
				         #root, and keep doing that until
					 #you eventually find it.

def Union(x,y):
	z1 = Find(x)
	z2 = Find(y) 	#Gets the roots of the trees containing x and y
			#respectively.
	if(z1 == z2):
		return #if they are the same, do nothing.
	else:
		parent[z2-1] = z1 #else, set one roots' parent to the 
				  #other root,which combines the two 
				  #trees into one.
		return

for (i,j) in edges:     #If there is an edge between vertex i and vertex j, 
			#connect the two trees (of the data structure!), 
			#making one tree where all its vertices
			#are in the same connected component of the graph.
	Union(i,j)

y=0 #This variable will store the number of components of the graph.

for x in range(1,11):
	if(parent[x-1] == x):
		y = y+1  #If x has itself as a root, then x is the unique root
			 #of a tree containing a graph's connected 
			 #component, so add one to the number of components.

print y  #Display the number of components on screen.

