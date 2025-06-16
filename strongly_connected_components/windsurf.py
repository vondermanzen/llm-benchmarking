def tarjan_scc(graph, n):
    index = 0
    indices = [-1] * (n + 1)
    lowlink = [-1] * (n + 1)
    on_stack = [False] * (n + 1)
    stack = []
    scc_count = 0

    def strongconnect(v):
        nonlocal index, scc_count
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc_count += 1
            while True:
                w = stack.pop()
                on_stack[w] = False
                if w == v:
                    break

    for v in range(1, n + 1):
        if indices[v] == -1:
            strongconnect(v)

    return scc_count

def main():
    # Read input
    N, M = map(int, input().split())
    
    # Build graph
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    # Count SCCs
    print(tarjan_scc(graph, N))

if __name__ == "__main__":
    main()
