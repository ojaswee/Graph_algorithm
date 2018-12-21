'''
Prim's algorithm is a greedy algorithm
It finds the minimum weight from the current node to its neighboring node and connects it. We repeat this until all the nodes are connected.
It is useful to use a priority queue to get the shortest distance
Please note: the vertex we will choose next has to be neighbor of current vertex.
'''

import Queue
from Queue import PriorityQueue

class vertex:
    def __init__(self,_name):
        self.name = _name
        self.neighbours = {}

    def add_neighbours(self, newVertex, weight):
        self.neighbours[newVertex] = weight

    def get_name(self):
        return self.name

    def get_numofneighbours(self):
        return len(self.neighbours)

    def get_neighbours(self):
        return self.neighbours.keys()

    def get_weight(self, newVertex):
        return self.neighbours[newVertex]

class graph:
    def __init__(self):
        self.vertices = {}
        self.countVertices = 0

    def add_vertices(self, name):
        newVertex = vertex(name)
        self.vertices[name] = newVertex
        self.countVertices += 1

    def add_edge(self, fromVertex, toVertex, weight):
        if fromVertex not in self.vertices:
            self.add_vertices(fromVertex)
        if toVertex not in self.vertices:
            self.add_vertices(toVertex)
        self.vertices[fromVertex].add_neighbours(toVertex, weight)


    def prim(self):
        q = Queue.PriorityQueue()
        for vertex in self.vertices:
            for neighbour in self.vertices[vertex].get_neighbours():
                print vertex, neighbour, self.vertices[vertex].get_weight(neighbour)
                q.put(self.vertices[vertex].get_weight(neighbour), str(vertex + neighbour))

        while not q.empty():
            print q.get()


newGraph = graph()
newGraph.add_vertices('A')
newGraph.add_edge('A','B',2)
newGraph.add_edge('B','C',5)
newGraph.add_edge('A','D',1)
newGraph.add_edge('C','E',3)
newGraph.add_edge('D','I',9)
newGraph.add_edge('E','F',5)
newGraph.add_edge('D','C',5)

# newGraph.prim()
