'''
We can do BFS/DFS 2 ways via adjacency list or vertices matrix
Here I am trying to solve BFS via vertices matrix.

When popping the stack pop from the front not from the back
because we want to visit the node in ascending order
For example 1 has children 6 and 21 then we want to go to
6 before 21.
'''
import numpy as np
# get graph from csv file
graphx = np.loadtxt("vertices_matrix.csv", dtype='i', delimiter=',')
# print(graphx)

def bfs_adjacency_mat(G, start, goal,count):
    visited=[False]*len(G[0])
    stack=[]
    stack.append(start)
    goal = goal -1
    while len(stack)!=0:
        # pop the first element not from the end of the stack
        v=stack.pop(0)
        if visited[v]==False:
            visited[v]=True
            count +=1
            print(v+1),
            for w in range(len(G[0])):
                if G[v][w]>0:
                    stack.append(w)
                elif v == goal:
                    while len(stack)!=0:
                        stack.pop()
                    return count 
                    break
    return count

# def bfs_adjacency_mat(G, start, goal,count):
#     print G

#Entry point for program execution
count = bfs_adjacency_mat(graphx, 0, 10,0)
print " "
print "Total nodes visited:",count