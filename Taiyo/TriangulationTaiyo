# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:55:02 2015

@author: taiyoshoe
"""
#This is a Triangulation Data structure in the method of Edelsbrunner and
#Harer. I have yet to add the program to find the genus of the surface,
#I will try to soon when I get a chance.

#Example data is given towards the bottom, it is hard coded into this file.


class triangles:# this describes the class of triangulations
    def __init__(self, faces, vertices): #initializes the triangulation
        self.tri=[face for face in faces]#Generates list of triangles 
        self.orient=[None for face in faces] #Generates list of oreintations
                                             #for each triangle
        
    def ENEXT(self,A): #gives the next rotation, just as in the text.
                       #A will be [m,i], where m is mu the triangle and i is 
                       #iota the orientation as in the text
        m=A[0]
        i=A[1] 
        if i<=2:
            return [m,(i+1)%3]
        else:
            return [m,((i+1)%3+4)]
    
    def SYM(self,A): # gives a flip symmetry, just like in the book
        m=A[0]
        i=A[1]
        return [m,(i+4)%8]
    
    def fnext(self,A):#Gives the next face with respect to the current 
                      #orientation. It takes advantage of of the Sym of a
                      #triangle being findable if you just know its 
                      #orientation class, so that I only need three pointers
                      #to the adjacent triangles 
                      #instead of the 6 that the book describes on page 34 
                      #under figure II.7
        m=A[0]
        i=A[1]
        if i<3:        
            return self.tri[m][i]
        else:
            return [self.tri[m][i-4][0],(self.tri[m][i-4][1]+4)%8]
        
    def org(self,A): # finds the vertex of a triangle described by a triangle
                     # given a certin orientation. Again just as in the book
        m=A[0]
        i=A[1]
        return self.tri[m][i%3+3]
        
            
    def isOrientable(self,A): #uses depth-first-search to test orientability.
                              # initially you musst choose a triangle and its
                              # orientation to start from.
        m=A[0]
        i=A[1]
        if self.orient[m]==None:# orient[m] is used to store orientation, but
                                #also it is used to see if that triangle has 
                                # been "marked" just like in the book
                                # so "None" is equivalent to unmarked
                                # the recursion part is computationally 
                                #identicle to how it is in the book.
                                # the only reason it looks a little different
                                # here was to save on repeating the same
                                # operation multiple times, though it shouldn't 
                                # matter because these symmetry operatins
                                # are simple modular arithmetic operations.
            self.orient[m]=i
            sym=self.SYM([m,i])
            enxsym=self.ENEXT(sym)
            enx2sym=self.ENEXT(enxsym)
            bx=self.isOrientable(self.fnext(sym))
            by=self.isOrientable(self.fnext(enxsym))
            bz=self.isOrientable(self.fnext(enx2sym))
            return bx and by and bz
        else:
            if self.orient[m]>3 and i>3:  # this is the part that is stated in 
                return True               # the book as 
            elif self.orient[m]<3 and i<3:#[orientaion of mu contains iota]
                return True               # it just checks that the new given
            else:                         # orientation, matches the direction
                return False              # that was stored for the triangle 
                                          # when it was visited before in the 
                                          # the search. We don't need the
                                          # the triangle to have the exact same
                                          # orientation number, we just need it
                                          # it ti be a cyclic rotation


#Here are some example data sets.
# notice that to test orientability, if the data is given in the form
#of spheref, fakekleinf, kleinf, ftorus, torus, Than they don't have to have
# an actual triangulation, they can just be a rectangle with two triangles that
# share all sides with one other triangle,
# if your data is given as a set of triangles (as I do below these examples),
# then you do need an actual triangulation. actually that is not true,
# you just need  each triangle to have three distinct vertices.
# neither is required for the edelsbrunner/Harer data structure
# infact you can even get rid of all vertice data and these algorithms work 
#fine.

#Each triangle consists of pointers from 3  orientations (the other three are 
#calculated) to the corresponding other triangles, that share and edge, and its
# relative orientations. one such pointer would be something like
#[1,0] meaning the triangle points to triangle 1, in orientation 0.
#so a full triangle would look like below
#[[tri1,orientation1],[tri2,orientation2] [tri3,orientation3]vertex1,vertex2,vertex3];


# this is a degenerate sphere, i.e two triangles which share three edges.
spheref=[[[1,0],[1,1],[1,2],1,2,3],[[0,0],[0,1],[0,2],1,2,3]]
spherev=[0,1,2]
exTri= triangles(spheref,spherev);
print("fake sphere: ", exTri.isOrientable([0,0]))

#This is a klien bottle, not a real triangulation, so I call it fake
#notice all vertices are the same.
fakekleinf=[[[1,5],[1,2],[1,4],0,0,0],[[0,6],[0,4],[0,1],0,0,0]]
fakekleinv=[0,0,0]
faketri=triangles(fakekleinf,fakekleinv)
print("fake klein bottle: ", faketri.isOrientable([0,0]))

#this is a real triangulation of a triangle, I looked it up to make sure.
kleinf=[[[13, 0], [1, 6], [5, 2], 0, 1, 5], [[15, 0], [2, 0], [0, 5], 1, 2, 5], [[1, 1], [8, 0], [3, 5], 2, 5, 6], [[16, 0], [2, 6], [4, 2], 0, 2, 6], [[12, 0], [10, 0], [3, 2], 0, 4, 6], [[17, 0], [6, 6], [0, 2], 0, 3, 5], [[11, 0], [7, 0], [5, 5], 3, 4, 5], [[6, 1], [8, 6], [12, 5], 4, 5, 7], [[2, 1], [9, 0], [7, 5], 5, 6, 7], [[8, 1], [14, 1], [10, 5], 6, 7, 8], [[4, 1], [9, 6], [11, 5], 4, 6, 8], [[6, 0], [10, 6], [17, 5], 3, 4, 8], [[4, 0], [7, 6], [13, 2], 0, 4, 7], [[0, 0], [14, 0], [12, 2], 0, 1, 7], [[13, 1], [9, 1], [15, 2], 1, 7, 8], [[1, 0], [16, 1], [14, 2], 1, 2, 8], [[3, 0], [15, 1], [17, 2], 0, 2, 8], [[5, 0], [11, 6], [16, 2], 0, 3, 8]]
kleinv=[0,1,2,3,4,5,6,7,8]
kleinTri= triangles(kleinf,kleinv)
print("klein bottle: ",kleinTri.isOrientable([0,0]))

# this is a Torus with out a triangulation, so for example, all vertices are 
#the same.
ftorusf=[[[1,1],[1,0],[1,2],0,0,0],[[0,1],[0,0],[0,2],0,0,0]]
ftorusv=[0,0,0]
ftorusTri=triangles(ftorusf,ftorusv)
print("fake torus: ",ftorusTri.isOrientable([0,0]))

#This is a real Triangulation of a Torus, I looked this one up to make sure.
torusf=[[[17,0],[1,0],[5,2],0,1,4],[[0,1],[2,2],[8,0],1,4,5],[[13,0],[3,6],[1,2],1,2,5],[[4,1],[10,0],[2,5],2,3,5],[[15,0],[3,0],[5,4],0,2,3],[[4,6],[6,0],[0,2],0,3,4],[[5,1],[7,0],[11,2],3,4,7],[[6,1],[14,1],[8,2],4,7,8],[[1,1],[9,6],[7,2],4,5,8],[[10,1],[16,1],[8,5],5,6,8],[[3,1],[9,0],[11,4],3,5,6],[[10,6],[12,1],[6,2],3,6,7],[[17,1],[11,1],[13,2],1,6,7],[[2,0],[14,0],[12,2],1,2,7],[[13,1],[7,1],[15,5],2,7,8],[[4,0],[14,6],[16,2],0,2,8],[[17,6],[9,1],[15,2],0,6,8],[[0,0],[12,0],[16,4],0,1,6]]
torusv=[0,1,2,3,4,5,6,7,8]
torusTri=triangles(torusf,torusv)
print("torus: ",torusTri.isOrientable([0,0]))

# below is all stuff I used to make it easier to get the data above in the 
#future.

def sameor(x,y): # this is used to check if two triangles should be 
                 #given the same default orientation in The Edelsbrunner/Harer
                 #Trianulation. 
                 # it is not too important it is just parsing the data.
    for a,i in enumerate(x):
        if i in y:
            indy=y.index(i)
            for b,j in enumerate(y):
                if i!=j:
                    if j in x:
                        indx=x.index(j)
                        if i<j:
                            if x[(2*a+2*indx)%3]>i and x[(2*a+2*indx)%3]<j:
                                if y[(2*b+2*indy)%3]<i or y[(2*b+2*indy)%3]>j:
                                    return 4
                                else:
                                    return 0
                            elif y[(2*b+2*indy)%3]>i and y[(2*b+2*indy)%3]<j:
                                return 4
                            else:
                                return 0
                        else:
                            if x[(2*a+2*indx)%3]<i and x[(2*a+2*indx)%3]>j:
                                if y[(2*b+2*indy)%3]>i or y[(2*b+2*indy)%3]<j:
                                    return 4
                                else:
                                    return 0
                            elif y[(2*b+2*indy)%3]<i and y[(2*b+2*indy)%3]>j:
                                return 4
                            else:
                                return 0
    return

torusGraph=[[0,1,4],[1,4,5],[1,2,5],[2,3,5],[0,2,3],[0,3,4],[3,4,7],[4,7,8],[4,5,8],[5,6,8],[3,5,6],[3,6,7],[1,6,7],[1,2,7],[2,7,8],[0,2,8],[0,6,8],[0,1,6]]

def graph_convert(G):#turns a regular triangulation into one such as the ones
                     #described by Edelsbrunner and Harer.
                     #by regular trianulation I mean given as a list of
                     # triangles by their vertices as above with the list torusGraph 
    triG=[[] for x in G]
    for i in range(len(G)):
        for j in range(len(G))[i+1:]:
            t=sameor(G[i],G[j])
            if t!=None:
                triG[i].append([j,t])
                triG[j].append([i,t])
    for i,x in enumerate(G):
        triG[i].append(x[0])
        triG[i].append(x[1])
        triG[i].append(x[2])
    return triG
torusG=graph_convert(torusGraph)

torusgraph=triangles(torusG,range(9))
print("torus from graph: ",torusgraph.isOrientable([0,0]))

