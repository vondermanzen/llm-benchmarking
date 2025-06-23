import numpy as np

N, M = map(int, input().split())
A = np.array([[int(x) for x in input().split()] for _ in range(N)])

rank = np.linalg.matrix_rank(A)
print(rank)