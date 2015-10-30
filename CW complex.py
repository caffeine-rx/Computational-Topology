# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:14:26 2015

@author: Ari
"""

# CW complex

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:07:53 2015

@author: Ari
"""

# Triangles cannot have repeated vertices!!!

import queue
from queue import Queue

class surface:
    def __init__(self,Vertices,Edges,Triangles):
        self.Triangles = Triangles
        self.Edges = Edges
        self.Vertices = Vertices
        self.l = len(Triangles)
        self.n = len(Vertices)
        self.m = len(Edges)
        self.EulerChar = self.n - self.m + self.l
        self.Orientable = None
        self.orientation = [None for k in range(self.l)]
  
        self.Edges2Triangles = {frozenset(edge):[] for edge in Edges}
        for i in range(self.l):
            a,b,c = self.Triangles[i]
            self.Edges2Triangles[frozenset((a,b))].append(i)
            self.Edges2Triangles[frozenset((b,c))].append(i)
            self.Edges2Triangles[frozenset((c,a))].append(i)
    
    def Direction(self,i,e): # Returns True if e is an edge of Triangles[i] in correct orientation
        a,b,c = self.Triangles[i]
        if (e==(a,b)) or (e==(b,c)) or (e==(c,a)):
            return True
        else:
            return False
            
    def Compare(self,i,j,e):   # Checks whether edge is oriented similarly in two triangles
        if self.Direction(i,e)==self.Direction(j,e):
            return True
        else:
            return False
    
    def isOrientable(self):
        if self.Orientable == None:
            Q = Queue()
            Q.put(0)
            self.orientation[0] = False  # Stores orienations of triangles
            self.Orientable = True
            while not Q.empty():
                if not self.Orientable:
                    break
                j = Q.get()
                a,b,c = self.Triangles[j]
                # Check edge 1
                e = (a,b)
                for k in self.Edges2Triangles[frozenset(e)]:
                    if j != k:
                        boo = self.orientation[j]^self.Compare(j,k,e)
                        if self.orientation[k] == None:
                            self.orientation[k] = boo
                            Q.put(k)
                        elif self.orientation[k] != boo:
                            self.Orientable = False
                            break
                        else:
                            pass
                # Check edge 2
                e = (b,c)
                for k in self.Edges2Triangles[frozenset(e)]:
                    if j != k:
                        boo = self.orientation[j]^self.Compare(j,k,e)
                        if self.orientation[k] == None:
                            self.orientation[k] = boo
                            Q.put(k)
                        elif self.orientation[k] != boo:
                            self.Orientable = False
                            break
                        else:
                            pass
                # Check edge 3
                e = (c,a)
                for k in self.Edges2Triangles[frozenset(e)]:
                    if j != k:
                        boo = self.orientation[j]^self.Compare(j,k,e)
                        if self.orientation[k] == None:
                            self.orientation[k] = boo
                            Q.put(k)
                        elif self.orientation[k] != boo:
                            self.Orientable = False
                            break
                        else:
                            pass
                        
    def getOrientable(self):
        if self.Orientable == None:
            self.isOrientable()
        return self.Orientable
        
    def getEulerChar(self):
        return self.EulerChar
       
       
# Hard coded examples
            
# Annulus
#Vertices = ['a','b','c','d','e']
#Edges = [('a','b'),('b','c'),('c','a'),('b','d'),('d','c'),('c','e'),('e','d'),('d','b'),('e','a'),('b','e')]
#Triangles = [('a','b','c'),('c','b','d'),('c','d','e'),('b','e','d'),('a','e','b')]

# Mobius strip
#Vertices = ['a','b','c','d','e']
#Edges = [('a','b'),('b','c'),('c','a'),('b','d'),('d','c'),('c','e'),('e','d'),('d','a'),('e','a'),('b','e')]
#Triangles = [('a','b','c'),('c','b','d'),('c','d','e'),('a','e','d'),('a','e','b')]

# Torus
#Vertices = ['a','b','c','d','e','f','g','h','i']
#Edges = [('a','b'),('b','c'),('c','a'),('d','e'),('e','f'),('f','d'),('g','h'),('h','i'),('i','g'),('a','d'),
#         ('d','g'),('g','a'),('b','e'),('e','h'),('h','b'),('c','f'),('f','i'),('i','c'),('a','e'),('b','f'), 
#        ('c','d'),('d','h'),('e','i'),('f','g'),('g','b'),('h','c'),('i','a')]
#Triangles = [('a','e','b'),('a','d','e'),('d','h','e'),('d','g','h'),('g','b','h'),('g','a','b'),('c','b','f'),
#             ('b','e','f'),('f','e','i'),('e','h','i'),('i','h','c'),('h','b','c'),('a','c','d'),('c','f','d'),
#            ('d','f','g'),('f','i','g'),('g','i','a'),('i','c','a')]
        
# Klein bottle
Vertices = ['a','b','c','d','e','f','g','h','i']
Edges = [('a','b'),('b','c'),('c','a'),('d','e'),('e','f'),('f','d'),('g','h'),('h','i'),('i','g'),('a','d'),
         ('d','g'),('g','a'),('b','e'),('e','h'),('h','b'),('c','f'),('f','i'),('i','c'),('a','e'),('b','f'), 
        ('c','d'),('d','h'),('e','i'),('f','g'),('g','c'),('h','b'),('i','a'),('h','c'),('i','b')]
Triangles = [('a','e','b'),('a','d','e'),('d','h','e'),('d','g','h'),('g','c','h'),('g','a','c'),('c','b','f'),
             ('b','e','f'),('f','e','i'),('e','h','i'),('i','h','c'),('h','b','c'),('a','c','d'),('c','f','d'),
            ('d','f','g'),('f','i','g'),('g','i','a'),('i','a','b')]

# Sphere
#Triangles = [('a','b','c'),('a','b','c')]
#Edges = [('a','b'),('b','c'),('c','a')]
#Vertices = ['a','b','c']

                    
X = surface(Vertices,Edges,Triangles)
print("Orientable:",X.getOrientable())
print("Euler characteristic:", X.getEulerChar())
    
    
        
        
