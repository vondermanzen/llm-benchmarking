from collections import defaultdict

def dfs(graph, v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited, stack)
    stack = stack.append(v)

def transpose(graph):
    g = defaultdict(list)
    for i in graph:
        for j in graph[i]:
            g[j].append(i)
    return g

def dfs_for_transpose(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs_for_transpose(graph, i, visited)

def count_scc(n, edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    visited =[False]*(n+1)
    stack = []
    for i in range(1,n+1):
        if visited[i]==False:
            dfs(graph, i, visited, stack)
    gr = transpose(graph)
    visited =[False]*(n+1)
    count = 0
    while stack:
        i = stack.pop()
        if visited[i]==False:
            dfs_for_transpose(gr, i, visited)
            count += 1
    return count

edges = [(1, 2), (2, 3), (3, 1), (4, 1)]
print(count_scc(4, edges))