from collections import defaultdict

def count_strongly_connected_components(n, edges):
    """
    Count the number of strongly connected components in a directed graph
    using Kosaraju's algorithm.

    Args:
        n (int): Number of vertices in the graph (1-indexed).
        edges (list): List of directed edges as pairs [u, v].

    Returns:
        int: Number of strongly connected components in the graph.
    """
    # Create graph and its transpose
    graph = defaultdict(list)
    transpose = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        transpose[v].append(u)  # Reverse edge for transpose graph

    # For vertices that have no outgoing or incoming edges, ensure they exist in the graph
    for i in range(1, n + 1):
        if i not in graph:
            graph[i] = []
        if i not in transpose:
            transpose[i] = []

    # First DFS to get finish times
    visited = [False] * (n + 1)  # +1 for 1-indexed vertices
    stack = []

    def dfs_fill_order(vertex):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs_fill_order(neighbor)
        stack.append(vertex)

    # Fill vertices in order of finish time
    for i in range(1, n + 1):
        if not visited[i]:
            dfs_fill_order(i)

    # Second DFS on transpose graph
    visited = [False] * (n + 1)
    scc_count = 0

    def dfs_transpose(vertex):
        visited[vertex] = True
        for neighbor in transpose[vertex]:
            if not visited[neighbor]:
                dfs_transpose(neighbor)

    # Process vertices in reverse order of finish time
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            dfs_transpose(vertex)
            scc_count += 1

    return scc_count

def main():
    # Read input
    n, m = map(int, input().split())

    # Read edges
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Count strongly connected components
    scc_count = count_strongly_connected_components(n, edges)

    # Print the result
    print(scc_count)

if __name__ == "__main__":
    main()
