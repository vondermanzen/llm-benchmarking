from collections import defaultdict

def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def transpose_graph(graph):
    transposed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)
    return transposed_graph

def dfs_scc(transposed_graph, node, visited, scc):
    visited[node] = True
    scc.append(node)
    for neighbor in transposed_graph[node]:
        if not visited[neighbor]:
            dfs_scc(transposed_graph, neighbor, visited, scc)

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

stack = []
visited = [False] * (N + 1)
for node in range(1, N + 1):
    if not visited[node]:
        dfs(graph, node, visited, stack)

transposed_graph = transpose_graph(graph)
visited = [False] * (N + 1)
scc_count = 0
while stack:
    node = stack.pop()
    if not visited[node]:
        scc = []
        dfs_scc(transposed_graph, node, visited, scc)
        scc_count += 1

print(scc_count)