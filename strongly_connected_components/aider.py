import sys
from collections import defaultdict

def kosaraju_scc_count(n, edges):
    def dfs(v, graph, visited, stack=None):
        visited[v] = True
        for neighbour in graph[v]:
            if not visited[neighbour]:
                dfs(neighbour, graph, visited, stack)
        if stack is not None:
            stack.append(v)

    def reverse_graph(n, edges):
        reversed_graph = defaultdict(list)
        for u, v in edges:
            reversed_graph[v].append(u)
        return reversed_graph

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (n + 1)
    stack = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, graph, visited, stack)

    reversed_graph = reverse_graph(n, edges)
    visited = [False] * (n + 1)
    scc_count = 0

    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs(v, reversed_graph, visited)
            scc_count += 1

    return scc_count

def main():
    input = sys.stdin.read
    data = input().splitlines()
    n, m = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:m+1]]
    print(kosaraju_scc_count(n, edges))

if __name__ == "__main__":
    main()
