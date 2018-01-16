'''
SO far we can only calculate path for possitive edge
What should we do if the pathways has negative numbers?
For this issue we use Bellman_Ford algorithm. In this algorithm
we first go over each vertex(v) and calculate distance from the source.
We do this v-1 times. O (vertices * relaxations)

'''
# i am using built in Graph, Vertex and PriorityQueue data structure
from pythonds.graphs import PriorityQueue, Graph
import sys # for maximum value

def bellman_Ford(aGraph, start):
    pq = PriorityQueue()
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    start.setDistance(0) #first vertex distance should be zero
    for v in aGraph.vertices:
        currentVert = pq.delMin() #decrease the vertices by 1
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
            print currentVert.getId(),nextVert.getId()


def floyd_Warshall(aGraph):
    distmat = [[100 for x in range(0,aGraph.numVertices+1)] for y in range(0,aGraph.numVertices+1)]

    for row in distmat:
        print row

    for num in range(0,aGraph.numVertices+1):
        distmat[num][num] = 0

    for v1 in aGraph.getVertices():

        currentvertex = aGraph.getVertex(v1)

        for childvertex in currentvertex.getConnections():

            print currentvertex.getWeight(childvertex)

            print int(v1), int(childvertex.getId())

            distmat[int(v1)][int(childvertex.getId())] = currentvertex.getWeight(childvertex)

            #distmat[int(currentvertex.getId())][int(childvertex)] = currentvertex.getWeight(childvertex)


    for row in distmat:
        print row


    numofvertices = aGraph.numVertices+1

    for k in range(1,numofvertices):
        for i in range(1, numofvertices):
            for j in range(1, numofvertices):
                if distmat[i][j] > distmat[i][k]+ distmat[k][j]:
                    distmat[i][j] = distmat[i][k] + distmat[k][j]


    for row in distmat:
        print row

'''
Ford-Fulkerson method is also known as maximum flow
A graph will start from source and end in sink 
Here we have 2 additional concept augment flow and residual graph 

We input 3 things Graph, start and sink
'''

def fordFulkerson(aGraph, start, sink):
    # FirstiInitialise flow in all edges to 0
    for v1 in aGraph.getVertices():
        currentvertex = aGraph.getVertex(v1)
        currentvertex.setDistance(0)
        print currentvertex.getDistance()



##########################################################################
newGraph = Graph()

newGraph.addEdge('1','3',-2)
newGraph.addEdge('3','4',2)
newGraph.addEdge('2','1',4)
newGraph.addEdge('2','3',3)
newGraph.addEdge('4','2',-1)

# for v in newGraph:
#     for w in v.getConnections():
#         print v.getId() , w.getId() ,v.getWeight(w)

#print 'No of vertices:', (newGraph.numVertices)

#bellman_Ford(newGraph, newGraph.getVertex('A'))

#floyd_Warshall(newGraph)

fordFulkerson(newGraph)