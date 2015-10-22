# Class:	MTH610
# Author:	Eric Funk
# Date:		2015-10-22
# Desc:		Data structure to represent the triangulation of a manifold.
# Instruct: This is just a class, so at the top of a file that wants to use this,
#			enter "import TriangulationDataStructure as tds" (replacing tds with
#			whatever you want to call it).
# To Do:	- Convert Vertices into a class, to allow exceeding 26 entries.
#			- Import schema from external file.
#			- Use relative Orientation as part of tying together adjacent faces.
#			- Or replace Orientation with one bit, relative to Id direction?
#			- Expand Triangulation to do the rest of what the book does.
#			- Remove arbitrary constraints around neighbors, adjacencies, vertices.

#import Eric_GraphHW as graph

class Face(object):

	# Create Face class to be used in Triangulation
	def __init__(self, vertices, orientation, neighbors = []):
		self.SetVertices(vertices)
		self.SetOrientation(orientation)
		self.neighbors = {}
		self.SetNeighbors(neighbors)

	def GetVertices(self):
		return self.vertices

	def SetVertices(self, vertices):
		self.vertices = list(vertices)
		if len(vertices) != 3:
			print('Face must have exactly 3 vertices. Given: ' + str(vertices) + '.')

	def GetOrientation(self):
		return self.orientation

	def SetOrientation(self, orientation):
		self.orientation = orientation
		if orientation not in [0,1,2,4,5,6]:
			print('Face must have proper orientation. Given: ' + str(orientation) + '.')

	def GetNeighbors(self):
		return self.neighbors

	#def SetNeighbors(self, neighbors = {}):
	#	self.neighbors = neighbors
	#
	#	if len(self.neighbors) > 3:
	#		print('Face may have at most 3 neighboring faces. Given: ' + str(neighbors) + '.')

	def SetNeighbors(self, neighbors = []):
		#self.neighbors = list(neighbors)
		for i, neighbor in enumerate(neighbors):
			#print('  -- ' + str(i) + ' / nbr: ' + str(neighbor))
			self.AddNeighbor(neighbor)

		if len(self.neighbors) > 3:
			print('Face may have at most 3 neighboring faces. Given: ' + str(neighbors) + '.')

	def AddNeighbor(self, neighbor):
		#self.neighbors.append(neighbor)
		#print('  -- -- ' + neighbor.Id() + ' : ' + str(self.neighbors.keys()))
		if neighbor.Id() in self.neighbors.keys():
			print('Face overwriting existing neighbor. Given: ' + str(neighbor.Id()) + ', Had: ' + str(self.neighbors[neighbor.Id()].Id()) + '.')
		self.neighbors[neighbor.Id()] = neighbor
		#print('  -- -- ' + neighbor.Id() + ' : ' + str(self.neighbors[neighbor.Id()]))
		#print('  -- -- ' + self.neighbors.keys() + ' : ' + str(self.neighbors.values()))

		if len(self.neighbors) > 3:
			print('Face may have at most 3 neighboring faces. Given: ' + str(neighbor.Id()) + ' makes for ' + str(len(self.neighbors)) + ' neighbors.')

	def Id(self):
		return ''.join(sorted(self.GetVertices()))

	def SameAs(self, face):
		return self.Id() == face.Id()

	def Adjacency(self, face):
		compare = face.GetVertices()
		commonVertices = []
		for i, vertex in enumerate(self.GetVertices()):
			if vertex in compare:
				commonVertices.append(vertex)

		# What to do about finding 3 matches?
		return commonVertices

	def DegreeAdjacency(self, face):
		return len(self.Adjacency(face))


class Triangulation(object):

	# Create Triangulation class, containing our data and all functions we desire to call
	def __init__(self, faceArray = []):
		self.SetFaces(faceArray)

	def GetFaces(self):
		return self.faces

	def SetFaces(self, faceArray):
		# Make distinct dictionary to avoid cross-contamination
		self.faces = {}
		for i, face in enumerate(faceArray):
			self.faces[face.Id()] = face
			#print(str(i) + ' ' + str(face.GetVertices()) + ' ' + face.Id())

		if len(self.faces) != len(faceArray):
			print('Not all faces imported into Triangulation.faces. Given: ' + str(len(faceArray)) + ', Have: ' + str(len(self.faces)) + '.')

	#def SetAdjacency(self):
		
	# Breadth First algorithm, designed to create initial adjacencies considering vertice triples
	def InitializeAdjacency(self):
		for i, ikey in enumerate(self.faces):
			face = self.faces[ikey]
			for j, jkey in enumerate(self.faces):
				compare = self.faces[jkey]
				degrees = face.DegreeAdjacency(compare)
				print('  -- Evaluate ' + face.Id() + ' + ' + compare.Id() + ' as neighbors. Degrees of adjacency: ' + str(degrees) + '.')
				if degrees == 2:
					face.AddNeighbor(compare)
					compare.AddNeighbor(face)
					print('     -- Add.')
				elif degrees == 3:
					print('     -- Same face; Skipping.')


# Debugging and test code, to exercise above classes
face = Face(['a','b','c'], 0)
face.SetNeighbors([face])
print('Vertices:    ' + str(face.GetVertices()))
print('Orientation: ' + str(face.GetOrientation()))
print('#Neighbors:  ' + str(len(face.GetNeighbors())))
neighbors = face.GetNeighbors()
for i, nbr in enumerate(neighbors):
	print('  -- ' + str(i) + ' / nbr: ' + str(nbr) + ' / neighbor: ' + str(neighbors[nbr]))
face.AddNeighbor(face)
neighbors = face.GetNeighbors()
for i, nbr in enumerate(neighbors):
	print('  -- ' + str(i) + ' / nbr: ' + str(nbr) + ' / neighbor: ' + str(neighbors[nbr]))

face1 = Face(['c','d','b'], 0)
face1.SetNeighbors(face.GetNeighbors().values())
print('Vertices:    ' + str(face1.GetVertices()))
print('Orientation: ' + str(face1.GetOrientation()))
print('#Neighbors:  ' + str(len(face1.GetNeighbors())))
neighbors1 = face1.GetNeighbors()
for i, nbr in enumerate(neighbors1):
	print('  -- ' + str(i) + ' / nbr: ' + str(nbr) + ' / neighbor: ' + str(neighbors[nbr]))

face00 = Face([], 0)
face20 = Face(['a','b'], 0)
face40 = Face(['a','b','c','d'], 0)
face31 = Face(['a','b','c'], 1)
face32 = Face(['a','b','c'], 2)
face33 = Face(['a','b','c'], 3)
face34 = Face(['a','b','c'], 4)
face35 = Face(['a','b','c'], 5)
face36 = Face(['b','c','a'], 6)
face46 = Face(['a','b','d'], 6)
print('Face35: ' + face35.Id())
print('Face36: ' + face36.Id())
print('Face46: ' + face46.Id())
print('Face35?36: ' + str(face35.SameAs(face36)))
print('Face36?35: ' + str(face36.SameAs(face35)))
print('Face35?46: ' + str(face35.SameAs(face46)))
print('Face36?46: ' + str(face36.SameAs(face46)))
print('Adjacency? 35,36: ' + str(face35.Adjacency(face36)))
print('Adjacency? 35,36: ' + str(face35.DegreeAdjacency(face36)))
print('Adjacency? 35,46: ' + str(face35.Adjacency(face46)))
print('Adjacency? 35,46: ' + str(face35.DegreeAdjacency(face46)))


triangulation = Triangulation([
		Face(['a','b','c'], 0),
		Face(['a','b','x'], 0),
		Face(['b','c','z'], 2),
		Face(['c','a','y'], 6)#,
		#Face(['b','d','x'], 0),
		#Face(['d','b','e'], 0),
		#Face(['z','e','b'], 0)
	])
triangulation.InitializeAdjacency()


