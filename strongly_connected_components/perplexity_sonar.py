import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def tarjan_scc(n, graph):
    index =  * (n + 1)
    lowlink =  * (n + 1)
    on_stack = [False] * (n + 1)
    stack = []
    current_index = 1
    scc_count = 0

    def strongconnect(v):
        nonlocal current_index, scc_count
        index[v] = current_index
        lowlink[v] = current_index
        current_index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if index[w] == 0:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])

        if lowlink[v] == index[v]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                if w == v:
                    break
            scc_count += 1

    for v in range(1, n + 1):
        if index[v] == 0:
            strongconnect(v)

    return scc_count

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

print(tarjan_scc(N, graph))