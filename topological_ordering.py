'''
In topological sorting, we need to look at the direction of the edge
The first vertex will always be a vertex without in-coming edges
It cannot start with a vertex which has an incoming path and
we cannot end topological sort of vertex which has an outgoing path
There are 2 ways to solve Topological sort 1) modification from dfs just add
an extra stack  2) source removal method, replace 1 with 0 in the vertices matrix

Here in graph_B, we cannot have a solution because we can start with F
after that, all other nodes have another path that is incoming besides F
'''
graph_A = {'A': ['C','B'],
           'C':['F'],
           'B':['E','G'],
           'G':['F'],
           'E':[],
           'D':['A','B','C','F','G'],
           'F': []}

graph_B = {'A': ['B'],
           'B':['C'],
           'C':['D'],
           'D':['G'],
           'G':['E'],
           'F':['E','B','C','G'],
           'E':['A']}

import Queue

GRAY, BLACK = 0, 1

def topological(graph):
    order, enter, state = Queue.deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order

def topological_sourceRemovalMethod(graph):
    topological_order = list()
    in_degree = {vertex: 0 for vertex in graph}
    # print(in_degree)

    for from_vertex in graph:
        for to_vertex in graph[from_vertex]:
            in_degree[to_vertex] += 1
    # print(in_degree)

    pq = Queue.PriorityQueue()
    for vertex in in_degree:
        if in_degree[vertex] == 0:
            pq.put(vertex)

    while not pq.empty():
        vertex = pq.get()
        # print(vertex)
        topological_order.append(vertex)
        for to_vertex in graph[vertex]:
            in_degree[to_vertex] -= 1
            if in_degree[to_vertex] == 0:
                pq.put(to_vertex)

    if len(topological_order) == len(graph):
        return topological_order
    else:
        return topological_order
        # return []


# check how it works
print topological(graph_A)
print (topological_sourceRemovalMethod(graph_B))

# try: topological(graph_B)
# except ValueError: print "Cycle!"