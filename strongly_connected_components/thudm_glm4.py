import sys
from collections import defaultdict, deque

def kosaraju(n, adj):
    visited = [False] * (n + 1)
    order = []
    
    def dfs(u):
        stack = [(u, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                order.append(node)
                continue
            if visited[node]:
                continue
            visited[node] = True
            stack.append((node, True))
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    stack.append((neighbor, False))
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    reversed_adj = defaultdict(list)
    for u in range(1, n + 1):
        for v in adj[u]:
            reversed_adj[v].append(u)
    
    visited = [False] * (n + 1)
    scc_count = 0
    
    for node in reversed(order):
        if not visited[node]:
            stack = [node]
            visited[node] = True
            component = []
            while stack:
                current = stack.pop()
                component.append(current)
                for neighbor in reversed_adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            scc_count += 1
    
    return scc_count

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr+2])
    ptr += 2
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input[ptr:ptr+2])
        ptr += 2
        adj[u].append(v)
    print(kosaraju(n, adj))

if __name__ == "__main__":
    main()