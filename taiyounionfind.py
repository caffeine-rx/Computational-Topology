# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:44:16 2015

@author: taiyoshoe
"""
#union-find data structure
#finds connected components

#loads graph from file, could be implemented differently for different representations of the data
# the adjacency list is seperated by line breaks
with open('graphAdjArrLine.txt') as inputfile:
    adjArray = []
    for line in inputfile:
        line = line.strip().split(" ") # to deal with any blanks, .split(",") if seperated by "," etc
        adjArray.append(line)
vertexNames={}
keys={}

# this builds the array setList that will contain the set information
setList=[]
for i,x in enumerate(adjArray):
    #[vertex,parent,rant,root]
    setList.append([i,i,0,i]);
    vertexNames[x[0]]=i
    keys[i]=x[0]
    
#this is will keep the number of roots, the code stops if roots=1
roots=len(setList)

# this will be used to find the components
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
    iRoot=setList[find(i)]
    jRoot=setList[find(j)]
    setList[i][3]=iRoot[0]
    setList[j][3]=jRoot[0]
    global roots
    if iRoot!=jRoot:
        roots -= 1
        if iRoot[2]<jRoot[2]:
            iRoot[1]=jRoot[0]
        elif iRoot[2]>jRoot[2]:
            jRoot[1]=iRoot[0]
        else:        
            jRoot[1]=iRoot[0]
            jRoot[3]=iRoot[0]
            iRoot[2]+=1

#unions all the edges in Graph once called
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
