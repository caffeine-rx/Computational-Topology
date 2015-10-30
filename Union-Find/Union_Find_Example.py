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

parent = vertices # parent[i] is the parent of i
rank = [0 for i in vertices] # if i is a root then rank[i] is the rank of i
roots = [True for i in vertices] # if i is a root then roots[i] will be True

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
            roots[x]  = False
        elif rank[y] < rank[x]:
            parent[y] = x      
            roots[y] = False
        else:
            parent[y] = x
            roots[y] = False
            rank[x] += 1

for i,j in edges:
    Union(i,j)
    
print(sum(roots)) # if this is 1, it means there was only 1 root in the final tree, so G was connected

    
    