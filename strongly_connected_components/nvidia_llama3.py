from collections import defaultdict

def dfs1(graph, visited, stack, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(graph, visited, stack, neighbor)
    stack.append(node)

def dfs2(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs2(graph, visited, neighbor)

def count_scc(n, edges):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    stack = []
    visited = [False] * (n + 1)
    for node in range(1, n + 1):
        if not visited[node]:
            dfs1(graph, visited, stack, node)

    visited = [False] * (n + 1)
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs2(reverse_graph, visited, node)
            scc_count += 1

    return scc_count

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(count_scc(n, edges))