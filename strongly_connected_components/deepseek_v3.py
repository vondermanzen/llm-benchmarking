import sys
from collections import defaultdict, deque

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    adj = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
    
    visited = [False] * (N + 1)
    order = deque()
    
    def dfs(u):
        if not visited[u]:
            visited[u] = True
            for v in adj[u]:
                dfs(v)
            order.appendleft(u)
    
    for u in range(1, N + 1):
        dfs(u)
    
    reverse_adj = defaultdict(list)
    for u in adj:
        for v in adj[u]:
            reverse_adj[v].append(u)
    
    visited = [False] * (N + 1)
    count = 0
    
    def reverse_dfs(u):
        if not visited[u]:
            visited[u] = True
            for v in reverse_adj[u]:
                reverse_dfs(v)
    
    for u in order:
        if not visited[u]:
            reverse_dfs(u)
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()