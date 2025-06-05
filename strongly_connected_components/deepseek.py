import sys
from collections import defaultdict, deque

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        rev_adj[v].append(u)
    
    stack = []
    visited = [False] * (N + 1)
    
    # First pass to fill the stack with vertices in order of finishing times
    for node in range(1, N + 1):
        if not visited[node]:
            dfs_stack = []
            dfs_stack.append((node, False))
            while dfs_stack:
                current, processed = dfs_stack.pop()
                if processed:
                    stack.append(current)
                    continue
                if visited[current]:
                    continue
                visited[current] = True
                dfs_stack.append((current, True))
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        dfs_stack.append((neighbor, False))
    
    # Second pass on the reversed graph
    visited = [False] * (N + 1)
    scc_count = 0
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs_stack = []
            dfs_stack.append(node)
            visited[node] = True
            while dfs_stack:
                current = dfs_stack.pop()
                for neighbor in rev_adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        dfs_stack.append(neighbor)
            scc_count += 1
    print(scc_count)

if __name__ == "__main__":
    main()