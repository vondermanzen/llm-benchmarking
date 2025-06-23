import sys

def kosaraju_scc(n, edges):
    def dfs(graph, node, visited, finish):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, finish)
        finish.append(node)

    def reverse_dfs(graph, node, visited, scc):
        visited.add(node)
        scc.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                reverse_dfs(graph, neighbor, visited, scc)

    graph = {i: [] for i in range(1, n + 1)}
    reverse_graph = {i: [] for i in range(1, n + 1)}

    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = set()
    finish = []

    for node in range(1, n + 1):
        if node not in visited:
            dfs(graph, node, visited, finish)

    scc_count = 0
    visited.clear()

    for node in finish[::-1]:
        if node not in visited:
            scc = set()
            reverse_dfs(reverse_graph, node, visited, scc)
            if len(scc) > 0:
                scc_count += 1

    return scc_count

def main():
    input = sys.stdin.read
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(kosaraju_scc(n, edges))

if __name__ == "__main__":
    main()