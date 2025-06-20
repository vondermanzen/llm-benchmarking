import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)

    visited = [False] * (N + 1)
    order = []

    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)

    # 1st pass: order vertices by finish time
    for u in range(1, N + 1):
        if not visited[u]:
            dfs(u)

    # Transpose the graph
    adj_rev = [[] for _ in range(N + 1)]
    for u in range(1, N + 1):
        for v in adj[u]:
            adj_rev[v].append(u)

    # 2nd pass: find SCCs in reverse order
    visited = [False] * (N + 1)
    scc_count = 0

    def dfs_rev(u):
        visited[u] = True
        for v in adj_rev[u]:
            if not visited[v]:
                dfs_rev(v)

    for u in reversed(order):
        if not visited[u]:
            scc_count += 1
            dfs_rev(u)

    print(scc_count)

if __name__ == "__main__":
    threading.Thread(target=main).start()