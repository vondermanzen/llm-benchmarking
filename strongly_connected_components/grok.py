def dfs_first_pass(graph, v, visited, finish):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs_first_pass(graph, u, visited, finish)
    finish.append(v)

def dfs_second_pass(graph, v, visited, component):
    visited[v] = True
    component.append(v)
    for u in graph[v]:
        if not visited[u]:
            dfs_second_pass(graph, u, visited, component)

def count_scc(n, edges):
    # Create adjacency lists for original and transposed graphs
    graph = [[] for _ in range(n + 1)]
    graph_t = [[] for _ in range(n + 1)]
    
    # Build graphs
    for u, v in edges:
        graph[u].append(v)
        graph_t[v].append(u)
    
    # First DFS pass to get finishing times
    visited = [False] * (n + 1)
    finish = []
    for v in range(1, n + 1):
        if not visited[v]:
            dfs_first_pass(graph, v, visited, finish)
    
    # Second DFS pass on transposed graph
    visited = [False] * (n + 1)
    scc_count = 0
    
    # Process vertices in reverse finishing order
    for v in reversed(finish):
        if not visited[v]:
            component = []
            dfs_second_pass(graph_t, v, visited, component)
            scc_count += 1
    
    return scc_count

def main():
    # Read input
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Compute and output result
    result = count_scc(n, edges)
    print(result)

if __name__ == "__main__":
    main()