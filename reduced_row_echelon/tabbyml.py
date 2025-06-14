def rank(matrix):
    # Convert matrix to reduced row echelon form (mod 2)
    reduced_matrix = []
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            reduced_matrix.append([1])
        else:
            reduced_matrix.append([0])
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == matrix[i][j-1]:
                reduced_matrix[-1].append(matrix[i][j])
            else:
                reduced_matrix.append([0])
                break
    # Find rank of reduced matrix
    rank = 0
    for row in reduced_matrix:
        if len(row) > rank:
            rank += 1
    return rank

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    matrix = []
    for i in range(N):
        matrix.append([int(x) for x in input().split()])
    print(rank(matrix))