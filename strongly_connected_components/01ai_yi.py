from collections import defaultdict

def dfs(node, graph, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, stack)
    stack.append(node)

def reverse_graph(graph):
    rev_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            rev_graph[neighbor].append(node)
    return rev_graph

def count_scc(graph, transposed_graph, vertices):
    visited = set()
    stack = []
    scc_count = 0

    for vertex in vertices:
        if vertex not in visited:
            dfs(vertex, graph, visited, stack)

    visited.clear()
    while stack:
        node = stack.pop()
        if node not in visited:
            dfs(node, transposed_graph, visited, [])
            scc_count += 1

    return scc_count

def main():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)

    transposed_graph = reverse_graph(graph)
    vertices = set(graph.keys())

    print(count_scc(graph, transposed_graph, vertices))

if __name__ == "__main__":
    main()