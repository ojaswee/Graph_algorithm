from queue import PriorityQueue

pq = PriorityQueue()

visited = [source]
path = [(0,source,'')]

def graph(source, destination, weight):
    pq.put((source, destination, weight))


def dijkstra(source, pq):
    current_node = source

    temp = PriorityQueue()

    #itreate until pq is not empty
    while not pq.empty():
        #get an item in the PriorityQueue
        extracted = pq.get()

        #check if 2nd column is same as our current_node
        if (extracted [1]==current_node):
            #add the path is this node has not been visited before
            if (extracted [2] not in visited):
                path.append(extracted)
                visited.append(extracted [2])
            #if it has been visited before

            else:
                for des in path:
                    weight = extracted[0]
                    if (des[2]== extracted[2]):
                        for s in path:
                            if (s[2] == extracted[1]):
                                weight = weight + s[0]
                        if weight < des[0]:
                            path.remove(des)
                            path.append(extracted)

        else:
            temp.put(extracted)

    if (not temp.empty()):
        new_index = visited.index(source) +1
        dijkstra (visited[new_index], temp)

source = 'A'

graph (2,'A', 'B')
graph (5,'A', 'D')
graph (4,'A', 'F')
graph (4,'B', 'C')
graph (3,'F', 'C')
graph (2,'D', 'F')
graph (1,'D', 'E')

dijkstra(source,pq)

print (visited)
print (path)
