import sys
sys.setrecursionlimit(10**5)

def kosaraju(graph, n):
    # First DFS to fill the stack
    visited = [False] * (n + 1)
    stack = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Create reversed graph
    reversed_graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in graph[i]:
            reversed_graph[j].append(i)
    
    # Second DFS to count SCCs
    visited = [False] * (n + 1)
    scc_count = 0
    
    def dfs2(node):
        visited[node] = True
        for neighbor in reversed_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor)
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs2(node)
            scc_count += 1
    
    return scc_count

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    print(kosaraju(graph, n))

if __name__ == "__main__":
    main()