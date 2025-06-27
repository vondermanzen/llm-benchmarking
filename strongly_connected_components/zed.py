def tarjan_scc(graph, n):
    """
    Tarjan's algorithm to find strongly connected components.

    Args:
        graph: Adjacency list representation of the directed graph
        n: Number of vertices

    Returns:
        Number of strongly connected components
    """
    # Initialize arrays
    index = [-1] * (n + 1)  # Discovery time of each vertex
    lowlink = [-1] * (n + 1)  # Lowest index reachable from vertex
    on_stack = [False] * (n + 1)  # Whether vertex is on stack
    stack = []  # Stack for DFS
    scc_count = 0
    current_index = 0

    def strongconnect(v):
        nonlocal current_index, scc_count

        # Set the depth index for v to the smallest unused index
        index[v] = current_index
        lowlink[v] = current_index
        current_index += 1
        stack.append(v)
        on_stack[v] = True

        # Consider successors of v
        for w in graph[v]:
            if index[w] == -1:
                # Successor w has not yet been visited; recurse on it
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                # Successor w is in stack and hence in the current SCC
                lowlink[v] = min(lowlink[v], index[w])

        # If v is a root node, pop the stack and print an SCC
        if lowlink[v] == index[v]:
            # Start a new strongly connected component
            scc_count += 1
            while True:
                w = stack.pop()
                on_stack[w] = False
                if w == v:
                    break

    # Run DFS from all unvisited vertices
    for v in range(1, n + 1):
        if index[v] == -1:
            strongconnect(v)

    return scc_count


def main():
    # Read input
    n, m = map(int, input().split())

    # Build adjacency list
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    # Count strongly connected components
    scc_count = tarjan_scc(graph, n)

    # Output result
    print(scc_count)


if __name__ == "__main__":
    main()

