import sys
sys.setrecursionlimit(50000)

def dfs1(node, visited, graph, group):
    visited[node] = True
    group.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(neighbor, visited, graph, group)

def dfs2(node, visited, graph, group):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs2(neighbor, visited, graph, group)

def count_sccs(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
    visited = [False] * (n + 1)
    group = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i, visited, graph, group)
    graph_rev = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in graph[u]:
            graph_rev[v].append(u)
    visited = [False] * (n + 1)
    scc_count = 0
    while group:
        u = group.pop()
        if not visited[u]:
            scc_count += 1
            dfs2(u, visited, graph_rev, [])
    return scc_count

n, m = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(map(int, input().split()))
print(count_sccs(n, m, edges))