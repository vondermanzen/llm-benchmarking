import sys
sys.setrecursionlimit(20000)

def kosaraju_scc_count(n, edges):
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u-1].append(v-1)
        rev_graph[v-1].append(u-1)

    visited = [False] * n
    order = []

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    visited = [False] * n
    scc_count = 0

    def rev_dfs(u):
        visited[u] = True
        for v in rev_graph[u]:
            if not visited[v]:
                rev_dfs(v)

    for u in reversed(order):
        if not visited[u]:
            rev_dfs(u)
            scc_count += 1

    return scc_count

if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(kosaraju_scc_count(N, edges))
