import Queue

class vertex:
    def __init__(self,_name):
        self.name = _name
        self.neighbours = {}

    def add_neighbours(self, newVertex, weight):
        self.neighbours[newVertex] = weight

    def get_name(self):
        return self.name

    def get_neighbours(self):
        return self.neighbours.keys()

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

    def BFS(self, root):
        q = Queue.Queue() #queue id FIFO
        q.put(root)
        while not q.empty():
            currentVertex = self.vertices[q.get()]
            print currentVertex.get_name()
            for x in currentVertex.get_neighbours():
                q.put(x)

    def DFS(self, root):
        s = Queue.LifoQueue()  # implimenting stack
        s.put(root)
        while not s.empty():
            currentVertex = self.vertices[s.get()]
            print currentVertex.get_name()
            for neighbours in currentVertex.get_neighbours():
                s.put(neighbours)


newGraph = graph()

newGraph.add_vertices('A')
newGraph.add_edge('A','B',2)
newGraph.add_edge('B','C',5)
newGraph.add_edge('B','D',1)
newGraph.add_edge('C','E',3)
newGraph.add_edge('D','I',9)
newGraph.add_edge('C','F',5)

print 'BFS'
newGraph.BFS('A')
print '-----'
print 'DFS'
newGraph.DFS('A')

print '-----'
print 'No of vertex:',newGraph.countVertices

