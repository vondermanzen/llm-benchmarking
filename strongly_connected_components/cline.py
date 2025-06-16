def kosaraju(graph, n):
    """
    Kosaraju's algorithm to find strongly connected components in a directed graph.
    
    Args:
        graph (dict): Adjacency list representation of the graph
        n (int): Number of vertices
        
    Returns:
        int: Number of strongly connected components
    """
    # Step 1: Perform DFS and store vertices in order of finishing time
    visited = [False] * (n + 1)
    stack = []
    
    def dfs1(vertex):
        visited[vertex] = True
        for neighbor in graph.get(vertex, []):
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(vertex)
    
    # Run DFS for all vertices
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Step 2: Transpose the graph (reverse all edges)
    transposed = {}
    for i in range(1, n + 1):
        for j in graph.get(i, []):
            if j not in transposed:
                transposed[j] = []
            transposed[j].append(i)
    
    # Step 3: Perform DFS on the transposed graph in order of finishing times
    visited = [False] * (n + 1)
    scc_count = 0
    
    def dfs2(vertex):
        visited[vertex] = True
        for neighbor in transposed.get(vertex, []):
            if not visited[neighbor]:
                dfs2(neighbor)
    
    # Process vertices in reverse order of finishing time
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            dfs2(vertex)
            scc_count += 1
    
    return scc_count

def main():
    # Read input
    n, m = map(int, input().split())
    
    # Build the graph as an adjacency list
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    
    # Count strongly connected components
    scc_count = kosaraju(graph, n)
    
    # Output result
    print(scc_count)

if __name__ == "__main__":
    main()
