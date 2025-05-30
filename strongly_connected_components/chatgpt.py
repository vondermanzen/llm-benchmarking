import sys
sys.setrecursionlimit(100000)

def kosaraju_scc_count(n, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    reverse_graph = defaultdict(list)

    # Build original and reversed graphs
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = [False] * (n + 1)
    finish_stack = []

    # First DFS - to fill the stack
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        finish_stack.append(node)

    # Second DFS - on the reversed graph
    def dfs2(node):
        visited[node] = True
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor)

    # Run first pass
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    # Reset visited for second pass
    visited = [False] * (n + 1)
    scc_count = 0

    # Run second pass
    while finish_stack:
        node = finish_stack.pop()
        if not visited[node]:
            dfs2(node)
            scc_count += 1

    return scc_count

# Input Reading
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n, m = int(data[0]), int(data[1])
    edges = [(int(data[i]), int(data[i+1])) for i in range(2, len(data), 2)]
    print(kosaraju_scc_count(n, edges))
