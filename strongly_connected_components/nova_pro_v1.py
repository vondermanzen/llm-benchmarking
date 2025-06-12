from collections import defaultdict, deque
import sys

def kosaraju(N, edges):
    graph = defaultdict(list)
    rev_graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        rev_graph[v].append(u)
    
    visited = [False] * (N + 1)
    stack = []
    
    def dfs(v, graph, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, stack)
        stack.append(v)
    
    for v in range(1, N + 1):
        if not visited[v]:
            dfs(v, graph, visited, stack)
    
    visited = [False] * (N + 1)
    scc_count = 0
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            scc_count += 1
            dfs(v, rev_graph, visited, [])
    
    return scc_count

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
print(kosaraju(N, edges))