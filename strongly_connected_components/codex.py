import sys
sys.setrecursionlimit(1000000)

# Read input
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    reverse_graph[v].append(u)

visited = [False] * (N + 1)
order = []

# First pass: order vertices by finish time
def dfs1(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs1(i)

# Second pass: explore reverse graph
def dfs2(u):
    visited[u] = True
    for v in reverse_graph[u]:
        if not visited[v]:
            dfs2(v)

visited = [False] * (N + 1)
scc_count = 0

for u in reversed(order):
    if not visited[u]:
        dfs2(u)
        scc_count += 1

print(scc_count)