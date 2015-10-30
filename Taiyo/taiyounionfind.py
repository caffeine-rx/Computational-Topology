# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:44:16 2015

@author: taiyoshoe
"""
# You can probably ignore it up to line 22
# line 39 is where the actual union find data structure is defined. the stuff before is just set up mostly.

#union-find data structure
#finds connected components

#adjacency list is seperated by line breaks but could e done differently
# This first part just opens and loads a graph from a file
with open('graphtaiyo.txt') as inputfile:
    adjArray = []
    for line in inputfile:
        line = line.strip().split(" ") # to deal with any blanks, .split(",") if seperated by "," etc
        adjArray.append(line)
vertexNames={}# this is a dictionary to store the possibly complex names of vertices in the graph file as names like 0,1,2,...,n for simplicity.
keys={} #this is dictionary to translate from the vertex names 0,1,2,...,n, back to the ones given in the graph

#this builds the array setList that will contain all the information about parents, roots, and size etc.
setList=[]
for i,x in enumerate(adjArray):
    # each element in the array stores the following information:
    # [vertex,parent,size,root]
    setList.append([i,i,0,i]);
    vertexNames[x[0]]=i
    keys[i]=x[0]
    
#this store the number of roots, the code stops if roots=1, since that means there is only one connected component.
roots=len(setList)

# this will be used to list the components at the end
comp=[];
for x in range(roots):
    comp.append([])

#finds root, hence sets
def find(i):
    parent=setList[i][1]
    if parent==i:
        return i
    else:
        parent=find(parent)
        return parent
        
#finds two vertices and if they are in the same set unions their sets.   
def union(i,j):
    iRoot=setList[find(i)]# finds location of i
    jRoot=setList[find(j)]# finds location of j
    setList[i][3]=iRoot[0]#updates the root of i
    setList[j][3]=jRoot[0]#updates the root of j
    global roots
    if iRoot!=jRoot:
        roots -= 1
        #iRoot[2] is the size of the longest branch of the set with the same root as i
        #it is the same "size" as referred to in the book
        if iRoot[2]<jRoot[2]:
            iRoot[1]=jRoot[0]
        elif iRoot[2]>jRoot[2]:
            jRoot[1]=iRoot[0]
        else:        
            jRoot[1]=iRoot[0]
            jRoot[3]=iRoot[0]
            iRoot[2]+=1

#unions all the edges in Graph once it is called
def makeforest(Graph):
    for i in Graph:
        for j in i[0:]:
            if roots==1:
                return
            else:
                union(vertexNames[i[0]],vertexNames[j])

#constructs the data structure.
makeforest(adjArray)

#translates the data structure names back to the vertices names in the dictionary
fList = [[keys[x[0]],keys[x[1]],x[2],keys[x[3]]] for x in setList]

#finds components from data structure.
for x in fList:
    comp[vertexNames[x[3]]].append(x[0])

components=[] # this will be the list of components
for x in comp:
    if len(x)>0:
        components.append(x)

print("Here are the components: \n", components)
print("the number of roots: ",roots)
