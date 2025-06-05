import sys
sys.setrecursionlimit(20000)

def tarjan_scc(graph):
    """
    Find strongly connected components using Tarjan's algorithm.
    
    Args:
        graph (dict): Adjacency list representation of the directed graph
        
    Returns:
        int: Number of strongly connected components
    """
    n = len(graph)
    if n == 0:
        return 0
    
    # Initialize data structures
    index_counter = [0]  # Use list to make it mutable in nested function
    stack = []
    lowlinks = {}
    index = {}
    on_stack = {}
    scc_count = [0]  # Use list to make it mutable in nested function
    
    def strongconnect(v):
        # Set the depth index for v to the smallest unused index
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True
        
        # Consider successors of v
        for w in graph.get(v, []):
            if w not in index:
                # Successor w has not yet been visited; recurse on it
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif on_stack.get(w, False):
                # Successor w is in stack and hence in the current SCC
                lowlinks[v] = min(lowlinks[v], index[w])
        
        # If v is a root node, pop the stack and create an SCC
        if lowlinks[v] == index[v]:
            scc_count[0] += 1
            while True:
                w = stack.pop()
                on_stack[w] = False
                if w == v:
                    break
    
    # Find SCCs for all vertices
    vertices = set()
    for v in graph:
        vertices.add(v)
        vertices.update(graph[v])
    
    for v in vertices:
        if v not in index:
            strongconnect(v)
    
    return scc_count[0]

def kosaraju_scc(graph, vertices):
    """
    Find strongly connected components using Kosaraju's algorithm.
    
    Args:
        graph (dict): Adjacency list representation of the directed graph
        vertices (set): Set of all vertices in the graph
        
    Returns:
        int: Number of strongly connected components
    """
    if not vertices:
        return 0
    
    # Step 1: Create reverse graph
    reverse_graph = {v: [] for v in vertices}
    for u in graph:
        for v in graph[u]:
            reverse_graph[v].append(u)
    
    # Step 2: First DFS to get finishing times
    visited = set()
    finish_stack = []
    
    def dfs1(v):
        visited.add(v)
        for u in graph.get(v, []):
            if u not in visited:
                dfs1(u)
        finish_stack.append(v)
    
    for v in vertices:
        if v not in visited:
            dfs1(v)
    
    # Step 3: Second DFS on reverse graph in reverse finishing order
    visited = set()
    scc_count = 0
    
    def dfs2(v):
        visited.add(v)
        for u in reverse_graph[v]:
            if u not in visited:
                dfs2(u)
    
    while finish_stack:
        v = finish_stack.pop()
        if v not in visited:
            dfs2(v)
            scc_count += 1
    
    return scc_count

def main():
    # Read input
    n, m = map(int, input().split())
    
    # Build adjacency list
    graph = {}
    vertices = set(range(1, n + 1))
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    
    # Handle case where there are no edges
    if m == 0:
        print(n)  # Each vertex is its own SCC
        return
    
    # Count SCCs using Kosaraju's algorithm
    scc_count = kosaraju_scc(graph, vertices)
    print(scc_count)

if __name__ == "__main__":
    main()
