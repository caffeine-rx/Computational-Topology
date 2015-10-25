# Class:	MTH610
# Author:	Eric Funk
# Date:		2015-10-17
# Desc:		Homework, implement algorithm to check if a graph is connected.
# Instruct: To run, simply call "python Eric_GraphHW.py" while in the correct directory. Output gives commentary.

class Graph(object):

	# Create Graph class, containing our data and all functions we desire to call
	def __init__(self, parentArray = []):
		# Make distinct arrays to avoid cross-contamination
		self.tree = list(parentArray)
		self.flattenedTree = list(parentArray)
		self.unionedTree = list(parentArray)
		self.flattenedUnionedTree = list(parentArray)

	# Standard Find algorithm
	def Find(self, tree, i):
		#print(str(i) + ' -> ' + str(tree[i]))
		if tree[i] != i:
			return self.Find(tree, tree[i])
		else:
			return i

	# Standard Union algorithm
	def Union(self, tree, i, j):
		x = self.Find(tree, i)
		y = self.Find(tree, j)
		
		if x != y:
			tree[y] = x
			return True

		return False

	# Bonus algorithm to find the children of a given node
	def FindChildren(self, tree, i):
		results = []
		for x, node in enumerate(tree):
			if node == i:
				results.append(x)

		#print(str(results))
		return results

	# Checks if two nodes have the same root, and thus are in the same connected graph
	def AreConnected(self, tree, i, j):
		return (self.Find(tree, i) == self.Find(tree, j))

	# Checks if the whole graph is connected, via tracking each of their roots looking for a conflict
	def IsConnectedGraph(self, tree):
		root = 0
		for x, node in enumerate(tree):
			parent = self.Find(tree, x)

			# If root is unset, start with first. Otherwise, look for conflict.
			if root == 0:
				root = parent
			elif root != parent:
				return False

		# No conflicts!
		return True

	# Counts how many connected components the graph is comprised of
	def GraphComponents(self, tree):
		components = []
		for x, node in enumerate(tree):
			parent = self.Find(tree, x)

			# If root is unset, start with first. Otherwise, look for conflict.
			if parent not in components:
				components.append(parent)

		return components

	# Modified Find algorithm that replaces each node's parents with its root, to speed later searching
	def FindFlatten(self, tree, i):
		#print(str(i) + ' -> ' + str(tree[i]))
		if tree[i] != i:
			tree[i] = self.FindFlatten(tree, tree[i])
			return tree[i]
		else:
			return i

	# Union algorithm that assumes and maintains flattening of tree
	def FlattenedUnion(self, tree, i, j):
		# Very quick if already flattened
		x = self.Find(tree, i)
		y = self.Find(tree, j)
		
		if x != y:
			tree[y] = x
			# Only moves over to new root what was already flattened, for convenience
			for z in self.FindChildren(tree, y):
				self.FindFlatten(tree, z)
			return True

		return False




# Put the class through its paces, as follows:
graph = Graph([0,11,3,15,2,4,6,6,1,12,9,12,7,7,3,15,6])
print('\nInitial tree is: ' + str(graph.tree) + '\n')

num1 = 12
print('Children of ' + str(num1) + ': ' + str(graph.FindChildren(graph.tree, num1)) + '\n')
#print()

num2 = 15
print('Find root of ' + str(num2) + ': ' + str(graph.Find(graph.tree, num2)))
num2 = 8
print('Find root of ' + str(num2) + ': ' + str(graph.Find(graph.tree, num2)))
#print(graph.tree)

num3 = 9
print()
print('Are ' + str(num2) + ', ' + str(num3) + ' connected? ' + str(graph.AreConnected(graph.tree, num2, num3)))
num3 = 14
print('Are ' + str(num2) + ', ' + str(num3) + ' connected? ' + str(graph.AreConnected(graph.tree, num2, num3)))

print('\nIs tree connected? ' + str(graph.IsConnectedGraph(graph.tree)))
print('Connected components are: ' + str(graph.GraphComponents(graph.tree)))

num3 = 9
print('\nUnion nodes ' + str(num2) + ', ' + str(num3) + ': ' + str(graph.Union(graph.unionedTree, num2, num3)))
print('Unioned tree: ' + str(graph.unionedTree))
num3 = 14
print('Union nodes ' + str(num2) + ', ' + str(num3) + ': ' + str(graph.Union(graph.unionedTree, num2, num3)))
print('Unioned tree: ' + str(graph.unionedTree))



print('\nFlatten tree while finding roots:')
for x, node in enumerate(graph.flattenedTree):
	if x != 0:
		print(str(x) + ':' + str(node) + ' -> ' + str(x) + ':' + str(graph.FindFlatten(graph.flattenedTree, x)))

graph.flattenedUnionedTree = list(graph.flattenedTree)
num3 = 9
print('\nFlattened union nodes ' + str(num2) + ', ' + str(num3) + ': ' + str(graph.FlattenedUnion(graph.flattenedUnionedTree, num2, num3)))
print('Flattened unioned tree: ' + str(graph.flattenedUnionedTree))
num3 = 14
print('Flattened union nodes ' + str(num2) + ', ' + str(num3) + ': ' + str(graph.FlattenedUnion(graph.flattenedUnionedTree, num2, num3)))
print('Flattened unioned tree: ' + str(graph.flattenedUnionedTree))




print('\nGraphs after testing:')
print('Initial tree:  ' + str(graph.tree))
print('Unioned tree:   ' + str(graph.unionedTree))
print('Flattened tree: ' + str(graph.flattenedTree))
print('FlatUnion tree: ' + str(graph.flattenedUnionedTree))


