def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        rev_adj[v].append(u)

    visited = [False] * (n + 1)
    stack = []

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        stack.append(u)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    visited = [False] * (n + 1)
    scc_count = 0

    def dfs2(u):
        visited[u] = True
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)

    while stack:
        u = stack.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1

    print(scc_count)

solve()