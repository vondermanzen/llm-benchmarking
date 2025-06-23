from collections import defaultdict

def count_strongly_connected_components(num_vertices, num_edges, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * num_vertices
    stack = []
    low = [0] * num_vertices
    time = [0]

    def tarjan(v):
        time[0] += 1
        low[v] = time[0]
        visited[v] = 1
        stack.append(v)

        for u in graph[v]:
            if visited[u] == 0:
                tarjan(u)
                low[v] = min(low[v], low[u])
            elif visited[u] == 1:
                low[v] = min(low[v], low[u])

        if low[v] == time[0]:
            comp = []
            while True:
                w = stack.pop()
                visited[w] = 2
                comp.append(w)
                if w == v:
                    break
            scc_count.append(comp)

    scc_count = []
    for i in range(1, num_vertices + 1):
        if visited[i] == 0:
            tarjan(i)

    # Count the number of SCCs
    return len(scc_count)

# Read input
num_vertices, num_edges = map(int, input().split())
edges = []
for _ in range(num_edges):
    u, v = map(int, input().split())
    edges.append((u, v))

# Count the strongly connected components
print(count_strongly_connected_components(num_vertices, num_edges, edges))