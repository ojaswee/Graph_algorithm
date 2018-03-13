import pandas as pd

def dfs_matrix(df, current, goal,count):
    col = len (df.columns)
    visited=[False]*col
    stack=[]
    stack.append(current)
    goal = goal -1
    while len(stack)!=0:
        v=stack.pop()
        if visited[v]==False:
            visited[v]=True
            count +=1
            print(v),
            for w in range(col):
                if df.shape!=0:
                    stack.append(w)
                elif v == goal:
                    # print(v)
                    while len(stack)!=0:
                        stack.pop()
                    return count
                    break

df = pd.read_csv(open('vertices_matrix.csv','rb'))
# print df
dfs_matrix (df, 1,10,0)