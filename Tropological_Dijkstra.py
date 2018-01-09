'''
In tropological sorting we need to look at the directiom of edge
The first vertex will always be a vertex without in-coming edges

'''
import Queue

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


newBFs = graph()

newBFs.add_vertices('A')
newBFs.add_edge('A','B',2)
newBFs.add_edge('B','C',5)
newBFs.add_edge('B','D',1)
newBFs.add_edge('C','E',3)
newBFs.add_edge('D','I',9)
newBFs.add_edge('C','F',5)
newBFs.add_edge('D','C',5)

print "Following is a Topological Sort of the given graph"
newBFs.topologicalSort('A')

# if currentVertex.get_neighbours() not in q.queue: