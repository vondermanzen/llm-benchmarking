import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    rev_graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        rev_graph[v].append(u)
    
    visited = [False] * (N + 1)
    order = []

    # 1st pass: normal DFS, push finished vertices to order stack
    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)
    
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
    
    # 2nd pass: reverse graph, find SCCs
    visited = [False] * (N + 1)
    scc_count = 0

    def reverse_dfs(u):
        visited[u] = True
        for v in rev_graph[u]:
            if not visited[v]:
                reverse_dfs(v)
    
    for u in reversed(order):
        if not visited[u]:
            scc_count += 1
            reverse_dfs(u)

    print(scc_count)

if __name__ == "__main__":
    threading.Thread(target=main).start()