"""
Count strongly connected components in a directed graph.
Input is read from standard input.
The first line contains N and M followed by M lines of edges.
Prints the number of SCCs.
"""
import sys
sys.setrecursionlimit(200000)

def read_input():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return 0, []
    first = data[0].split()
    n = int(first[0])
    m = int(first[1])
    edges = []
    for line in data[1:1 + m]:
        if line.strip() == "":
            continue
        u, v = map(int, line.split())
        edges.append((u, v))
    return n, edges

def build_graph(n, edges):
    graph = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        rev[v].append(u)
    return graph, rev

def dfs1(v, graph, visited, order):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs1(nxt, graph, visited, order)
    order.append(v)

def dfs2(v, rev, visited):
    visited[v] = True
    for nxt in rev[v]:
        if not visited[nxt]:
            dfs2(nxt, rev, visited)

def count_scc(n, edges):
    graph, rev = build_graph(n, edges)
    visited = [False] * (n + 1)
    order = []
    for v in range(1, n + 1):
        if not visited[v]:
            dfs1(v, graph, visited, order)
    visited = [False] * (n + 1)
    scc = 0
    for v in reversed(order):
        if not visited[v]:
            dfs2(v, rev, visited)
            scc += 1
    return scc

def main():
    n, edges = read_input()
    if n == 0:
        print(0)
        return
    print(count_scc(n, edges))

if __name__ == "__main__":
    main()
