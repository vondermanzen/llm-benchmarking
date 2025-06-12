from sys import stdin, stdout

def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

def count_sccs(n, edges):
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = [False] * (n + 1)
    scc_count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            scc_count += 1

    visited = [False] * (n + 1)
    scc_count = 0

    for i in range(n, 0, -1):
        if not visited[i]:
            dfs(reverse_graph, i, visited)
            scc_count += 1

    return scc_count

n, m = map(int, stdin.readline().split())
edges = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

result = count_sccs(n, edges)
stdout.write(str(result))