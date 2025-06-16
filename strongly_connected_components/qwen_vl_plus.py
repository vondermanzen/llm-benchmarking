from collections import defaultdict, deque


def count_strongly_connected_components(N, M):
    if not M:
        return N
    
    adj_list = {i + 1: [] for i in range(N)}
    
    # Build adjacency list with reversed direction as well since we need both forward and backward directions.
    reverse_adj_list = {i + 1: [] for i in range(N)}
    indegree = [0] * (N + 1)

    def add_edge(u, v):
        nonlocal adj_list, reverse_adj_list, indegree
        adj_list[u].append(v)
        reverse_adj_list[v].append(u)
        indegree[u] += 1

    for _ in range(M):
        u, v = map(int, input().split())
        add_edge(u, v)
        
    stack = []
    visited = set()
    scc_count = 0

    while True:
        node = None
        
        # Find an unvisited node starting at root nodes having no incoming edges.
        for n in range(1, len(indegree)):
            if n not in visited and indegree[n] == 0:
                node = n
                break
                
        else:
            break
            
        if node is None:
            continue
            
        visited.add(node)
        stack.append(node)
            
        while stack:
            current_node = stack.pop()

            # Visit all neighbors before popping it off so they can also get pushed onto our stack later on when their backedges come around.
            for neighbor in adj_list[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    
            # When you pop your last element out after visiting its children, then you know what SCC you're currently building up!
            scc_count += 1
                    
    print(scc_count)


if __name__ == "__main__":
    N, M = map(int, input().split())
    count_strongly_connected_components(N, M)