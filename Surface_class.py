# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:07:53 2015

@author: Ari
"""

import numpy as np
from numpy import array,zeros,shape
import queue
from queue import Queue

# Annulus
#Vertices = array(['a','b','c','d','e'])
#Edges = array([['a','b'],['b','c'],['c','a'],['b','d'],['d','c'],['c','e'],['e','d'],['d','b'],['e','a'],['b','e']])
#Triangles = array([['a','b','c'],['c','b','d'],['c','d','e'],['b','e','d'],['a','e','b']])

# Mobius strip
#Vertices = array(['a','b','c','d','e'])
#Edges = array([['a','b'],['b','c'],['c','a'],['b','d'],['d','c'],['c','e'],['e','d'],['d','a'],['e','a'],['b','e']])
#Triangles = array([['a','b','c'],['c','b','d'],['c','d','e'],['a','e','d'],['a','e','b']])

# Torus
Vertices = array(['a','b','c','d','e','f','g','h','i'])
Edges = array([['a','b'],['b','c'],['c','a'],['d','e'],['e','f'],['f','d'],['g','h'],['h','i'],['i','g'],['a','d'],
         ['d','g'],['g','a'],['b','e'],['e','h'],['h','b'],['c','f'],['f','i'],['i','c'],['a','e'],['b','f'], 
        ['c','d'],['d','h'],['e','i'],['f','g'],['g','b'],['h','c'],['i','a']])
Triangles = array([['a','e','b'],['a','d','e'],['d','h','e'],['d','g','h'],['g','b','h'],['g','a','b'],['c','b','f'],
             ['b','e','f'],['f','e','i'],['e','h','i'],['i','h','c'],['h','b','c'],['a','c','d'],['c','f','d'],
            ['d','f','g'],['f','i','g'],['g','i','a'],['i','c','a']])
        
# Klein bottle
#Vertices = array(['a','b','c','d','e','f','g','h','i'])
#Edges = array([['a','b'],['b','c'],['c','a'],['d','e'],['e','f'],['f','d'],['g','h'],['h','i'],['i','g'],['a','d'],
#         ['d','g'],['g','a'],['b','e'],['e','h'],['h','b'],['c','f'],['f','i'],['i','c'],['a','e'],['b','f'], 
#        ['c','d'],['d','h'],['e','i'],['f','g'],['g','c'],['h','b'],['i','a']])
#Triangles = array([['a','e','b'],['a','d','e'],['d','h','e'],['d','g','h'],['g','c','h'],['g','a','c'],['c','b','f'],
#             ['b','e','f'],['f','e','i'],['e','h','i'],['i','h','c'],['h','b','c'],['a','c','d'],['c','f','d'],
#            ['d','f','g'],['f','i','g'],['g','i','a'],['i','a','b']])
#            

l = shape(Triangles)[0]
n = shape(Vertices)[0]
m = shape(Edges)[0]

Adjacent = {}
for i in range(n):
    for j in range(n):
        if i!=j:
            Adjacent[Vertices[i],Vertices[j]]=[]

for i in range(l):
    Tri = Triangles[i,:]
    Adjacent[Tri[0],Tri[1]].append(i)
    Adjacent[Tri[1],Tri[0]].append(i)
    Adjacent[Tri[1],Tri[2]].append(i)
    Adjacent[Tri[2],Tri[1]].append(i)
    Adjacent[Tri[2],Tri[0]].append(i)
    Adjacent[Tri[0],Tri[2]].append(i)
    
def LeadingVertex(i,v,w):
    a,b,c = Triangles[i,:]
    if ((v,w) == (a,b)) or ((v,w) == (b,c)) or ((v,w) == (c,a)):
        return v
    else:
        return w
        
def Compare(i,j,v,w):
    if LeadingVertex(i,v,w)==LeadingVertex(j,v,w):
        return True
    else:
        return False
    
orientation = array([None for k in range(l)])

Q = Queue()
Q.put(0)
orientation[0] = False

Orientable = True

while not Q.empty():
    i = Q.get()
    a,b,c = Triangles[i,:]
    for j in Adjacent[a,b]:
        if j != i:
            boo = orientation[i]^Compare(i,j,a,b)
            if orientation[j] == None:
                Q.put(j)
                orientation[j] = boo
            elif orientation[j] != boo:
                Orientable = False
            else:
                pass
    for j in Adjacent[b,c]:
        if j != i:
            boo = orientation[i]^Compare(i,j,a,b)
            if orientation[j] == None:
                Q.put(j)
                orientation[j] = boo
            elif orientation[j] != boo:
                Orientable = False
            else:
                pass
    for j in Adjacent[c,a]:
        if j != i:
            boo = orientation[i]^Compare(i,j,a,b)
            if orientation[j] == None:
                Q.put(j)
                orientation[j] = boo
            elif orientation[j] != boo:
                Orientable = False
            else:
                pass
            
print("Orientable: ",Orientable)
print("Euler characteristi: ",n-m+l)


    
    
