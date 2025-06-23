import sys

def dfs1(node, visited, graph, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(neighbor, visited, graph, stack)
    stack.append(node)

def dfs2(node, visited, graph, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs2(neighbor, visited, graph, component)

def kosaraju(graph, num_nodes):
    stack = []
    visited = [False] * (num_nodes + 1)
    for node in range(1, num_nodes + 1):
        if not visited[node]:
            dfs1(node, visited, graph, stack)

    graph_transpose = {node: [] for node in range(1, num_nodes + 1)}
    for node in graph:
        for neighbor in graph[node]:
            graph_transpose[neighbor].append(node)

    visited = [False] * (num_nodes + 1)
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, visited, graph_transpose, component)
            scc_count += 1

    return scc_count

if __name__ == "__main__":
    input_data = sys.stdin.read().split('\n')
    N, M = map(int, input_data[0].split())
    graph = {node: [] for node in range(1, N + 1)}
    for line in input_data[1:]:
        u, v = map(int, line.split())
        graph[u].append(v)

    print(kosaraju(graph, N))