'''
Using adjacency list for bfs and dfs

'''

import numpy as np
# finds shortest path between 2 nodes of a graph using BFS

def bfs_shortest_path(graph, start, goal,count):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    count =count +1
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal", count

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]

        if node not in explored:
            neighbours = graph_bfs[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                count =count+1
                print neighbour,
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path,count
            # mark node as explored
            explored.append(node)
    print ""
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :(",count


# --------------------DFS
def dfs_iterative(graph_dfs, start, goal, count):
    stack = [start]
    visited = []
    # count += 1
    while stack:
        vertex = stack.pop()
        if vertex not in visited and vertex != goal:
            visited.append(vertex)
            stack.extend([x for x in graph_dfs[vertex] if x not in visited])
            count += 1
        else:
            visited.append(vertex)
            count +=1
            return visited, count

if __name__ == '__main__':
    graph_dfs = {'1': ['21','6'],
                 '6': ['20', '18'],
             '21': ['Swan','Bear'],
             'Bear': ['21'],
             'Swan':['21'],
             '20':['Fox','Exit'],
             '18':['7'],
             '7':['18','17','16','15'],
             '15': ['14','13'],
             '13': ['15'],
             '14': ['15'],
             'Exit':['20'],
             '17': ['7'],
             '16': ['7'],
             'Fox':['9','4'],
             '11': ['12'],
             '9':['19','Squirel'],
             'Squirel': ['9'],
             '19': ['9'],
             '4':['12'],
             '12':['11']}

    graph_bfs = {'1': ['6','21'],
             '21': ['Bear','Swan'],
             '6':['18','20'],
             '20':['Exit','Fox'],
             '18':['7'],
             '7':['15','16','17','18'],
             '15': ['14','13'],
             'Fox':['9','4'],
             '9':['19','Squirel'],
             '4':['12'],
             '12':['11']}

# BFS driver program
start = '1'
count = 0
print "All the visited nodes: ",start,
path,count = bfs_shortest_path(graph_bfs, start, 'Exit', count)
print ""
# print "Final Path BFS",path
print "Number of visited Nodes:",count


# DFS driver program
# start = '1'
# path,count= list(dfs_iterative(graph_dfs, start,'Exit',count=0))
#
# print ""
# print "Final Path DFS ",path
# print "Number of visited Nodes:",count
