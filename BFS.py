'''
@Author: your name
@Date: 2020-03-29 11:44:28
@LastEditTime: 2020-03-29 13:47:45
@LastEditors: Please set LastEditors
@Description: 图的BFS和DFS
@FilePath: \刷题人生\BFS.py
'''
graph ={
    "A":["B","C"],
    "B":['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
    }
print(graph.keys())

def BFS(graph,s):#最短路径
    quene = []
    quene.append(s)
    seen = set()
    seen.add(s)
    parent = {s:None}

    while(len(quene)>0):
        vertex = quene.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                quene.append(w)
                seen.add(w)
                parent[w]=vertex
        print(vertex)
    return parent
print('图的BFS')
parent = BFS(graph,'A')
for key in parent:
    print(key,parent[key])

def DFS(graph,s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while(len(stack)>0):
        vertex = stack.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)
print('图的DFS')
DFS(graph,'A')       
