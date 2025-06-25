#!/usr/bin/env python3

def read_input():
    """
    Read the input in the specified format.
    
    Returns:
        tuple: (n, m, edges) where n is the number of vertices,
               m is the number of edges, and edges is the list of edges
    """
    n, m = map(int, input().strip().split())
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append((u, v))
    
    return n, m, edges

def build_graph(n, edges):
    """
    Build the graph and its transpose from the edges.
    
    Args:
        n: Number of vertices
        edges: List of edges (u, v)
        
    Returns:
        tuple: (graph, transpose) where graph is the adjacency list representation
               and transpose is the transpose of the graph
    """
    # Initialize empty adjacency lists for both graph and its transpose
    graph = [[] for _ in range(n + 1)]
    transpose = [[] for _ in range(n + 1)]
    
    # Add edges to both graph and transpose
    for u, v in edges:
        graph[u].append(v)
        transpose[v].append(u)
    
    return graph, transpose

def dfs_first_pass(graph, n):
    """
    First DFS pass to compute finishing times.
    
    Args:
        graph: Adjacency list representation of the graph
        n: Number of vertices
        
    Returns:
        list: Vertices in order of decreasing finishing time
    """
    visited = [False] * (n + 1)
    finish_order = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        finish_order.append(node)
    
    # Run DFS for each unvisited vertex
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    return finish_order

def dfs_second_pass(graph, order):
    """
    Second DFS pass to identify SCCs.
    
    Args:
        graph: Adjacency list representation of the transpose graph
        order: Vertices in order of decreasing finishing time
        
    Returns:
        int: Number of strongly connected components
    """
    visited = [False] * len(graph)
    scc_count = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    # Process vertices in decreasing order of finishing time
    for node in reversed(order):
        if not visited[node]:
            dfs(node)
            scc_count += 1
    
    return scc_count

def count_scc(n, edges):
    """
    Count the number of strongly connected components in the graph.
    
    Args:
        n: Number of vertices
        edges: List of edges (u, v)
        
    Returns:
        int: Number of strongly connected components
    """
    # Handle empty graph case
    if n == 0:
        return 0
    
    # Build the graph and its transpose
    graph, transpose = build_graph(n, edges)
    
    # First DFS pass to get finishing times
    finish_order = dfs_first_pass(graph, n)
    
    # Second DFS pass to identify SCCs
    scc_count = dfs_second_pass(transpose, finish_order)
    
    return scc_count

def main():
    # Read input
    n, m, edges = read_input()
    
    # Count SCCs
    result = count_scc(n, edges)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()
