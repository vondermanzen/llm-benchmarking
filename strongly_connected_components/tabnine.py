def count_strongly_connected_components(N, edges):
    # Step 1: Create adjacency lists for both the original graph and its transpose
    graph = [[] for _ in range(N+1)]
    transpose = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)
        transpose[v].append(u)

    # Step 2: Perform a depth-first search (DFS) on the original graph
    visited = [False] * (N+1)
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)

    # Step 3: Perform a DFS on the transpose graph, considering the nodes in the order of the stack
    visited = [False] * (N+1)
    scc_count = 0

    def dfs_transpose(node):
        visited[node] = True
        for neighbor in transpose[node]:
            if not visited[neighbor]:
                dfs_transpose(neighbor)

    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs_transpose(node)
            scc_count += 1

    return scc_count

# Read input
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

# Count strongly connected components
result = count_strongly_connected_components(N, edges)
print(result)