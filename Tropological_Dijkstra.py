'''
In tropological sorting we need to look at the directiom of edge
The first vertex will always be a vertex without in-coming edges

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


    def topologicalSort(self, root):
        s = Queue.LifoQueue()  # implimenting stack
        s.put(root)

        visited = []

        while not s.empty():
            currentVertex = self.vertices[s.get()]

            if currentVertex.get_name() not in visited:
                visited.append(currentVertex.get_name())

                for neighbour in currentVertex.get_neighbours():

                    if neighbour not in visited:
                        s.put(neighbour)
                    else:
                        print neighbour
            else:
                print currentVertex.get_name()


    '''
    Prims find the minimum spanning tree, 
    It is a greedy algorithm
    we need to use priority queue because it has to get the shortest distance first
    Here the next vertex we chose should be neighbour of current vertex
    '''

    def prim(self):
        q = Queue.PriorityQueue()
        for vertex in self.vertices:
            for neighbour in self.vertices[vertex].get_neighbours():
                print vertex, neighbour, self.vertices[vertex].get_weight(neighbour)
                q.put(self.vertices[vertex].get_weight(neighbour), str(vertex + neighbour))

        while not q.empty():
            print q.get()


    def dijkstra(self, root,priority):
        pq = PriorityQueue()
        self.priority = 0
        while not pq.empty():
            currentVertex = self.vertices[pq.get()]
            for next in currentVertex.get_neighbours():
                newDist = currentVertex.get_weight(next)
                # get neighbour with lowest distance
                if newDist < next.get_weight():
                    next.setDistance(newDist)
                    next.setPred(currentVertex)
                    # pq.decreaseKey(next, newDist)

newGraph = graph()
newGraph.add_vertices('A')
newGraph.add_edge('A','B',2)
newGraph.add_edge('B','C',5)
newGraph.add_edge('A','D',1)
newGraph.add_edge('C','E',3)
newGraph.add_edge('D','I',9)
newGraph.add_edge('E','F',5)
newGraph.add_edge('D','C',5)

print "Following is a Topological Sort of the given graph"
# newBFs.topologicalSort('A')

# newGraph.dfs_tropo_sort('A')
# newGraph.dijkstra('A',0)
newGraph.prim()


