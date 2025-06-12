import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(graph, v, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(v)

def transpose(graph):
    transposed = defaultdict(list)
    for v in graph:
        for neighbor in graph[v]:
            transposed[neighbor].append(v)
    return transposed

def count_scc(graph, n):
    visited = [False] * (n + 1)
    stack = []
    
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(graph, v, visited, stack)
    
    transposed_graph = transpose(graph)
    visited = [False] * (n + 1)
    scc_count = 0
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs(transposed_graph, v, visited, [])
            scc_count += 1
    
    return scc_count

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

result = count_scc(graph, n)
print(result)