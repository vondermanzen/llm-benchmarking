def count_scc(n, edges):
    """
    Counts the number of strongly connected components (SCCs) in a directed graph.

    Args:
        n: The number of vertices in the graph (1 <= n <= 10,000).
        edges: A list of tuples, where each tuple (u, v) represents a directed edge from vertex u to vertex v.

    Returns:
        The number of strongly connected components in the graph.
    """

    if n == 0:
        return 0

    adj = [[] for _ in range(n + 1)]
    adj_rev = [[] for _ in range(n + 1)]

    for u, v in edges:
        adj[u].append(v)
        adj_rev[v].append(u)

    visited = [False] * (n + 1)
    stack = []

    def dfs1(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    visited = [False] * (n + 1)
    scc_count = 0

    def dfs2(node):
        visited[node] = True
        for neighbor in adj_rev[node]:
            if not visited[neighbor]:
                dfs2(neighbor)

    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs2(node)
            scc_count += 1

    return scc_count

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = count_scc(n, edges)
    print(result)