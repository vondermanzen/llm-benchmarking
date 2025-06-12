def count_sccs(N, M, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    reverse_graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def reverse_dfs(v, visited):
        visited[v] = True
        for neighbor in reverse_graph[v]:
            if not visited[neighbor]:
                reverse_dfs(neighbor, visited)

    visited = [False] * (N + 1)
    stack = []

    # Step 1: Order vertices by finish time in decreasing order
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, visited, stack)

    visited = [False] * (N + 1)
    scc_count = 0

    # Step 2: Process vertices in decreasing order of finish time
    while stack:
        v = stack.pop()
        if not visited[v]:
            reverse_dfs(v, visited)
            scc_count += 1

    return scc_count

# Example usage
N = 4
M = 4
edges = [(1, 2), (2, 3), (3, 1), (4, 1)]
print(count_sccs(N, M, edges))  # Output: 2