# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:09:26 2015

@author: Ari
"""
import random
from random import randint

# Graph
vertices = [0,1,2,3,4,5] # Must be a subset of N
edges = [(0,1),(1,2),(2,4),(4,3),(5,0)] # Must be a relation on N
num_vertices = len(vertices) # Number of vertices

parent = vertices # parent[i] is the parent of i
rank = [0 for i in vertices] # if i is a root then rank[i] is the rank of i

def Find(i):  # Uses path compression
    if parent[i] == i:
        return i
    else:
        parent[i] = Find(parent[i])
        return parent[i]
    
def Union(i,j):
    x = Find(i)
    y = Find(j)
    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x      
        else:
            parent[y] = x
            rank[x] += 1

for i,j in edges:
    Union(i,j)
    
num_components = 0
for i in range(num_vertices):
    if parent[i]==i:
        num_components += 1

print(num_components) # if this is 1, it means there was only 1 root in the final tree, so G was connected

    
    