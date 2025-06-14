def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot == yroot:
        return

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

N, M = list(map(int, input().split()))
edges = []
parent = [i for i in range(N)]
rank = [0] * N

for _ in range(M):
    u, v = list(map(int, input().split()))
    edges.append((u - 1, v - 1))

edges.sort(key=lambda x: x[1])
num_components = 0

for u, v in edges:
    if find(parent, u) == find(parent, v):
        continue
    union(parent, rank, u, v)
    num_components += 1

print(num_components)