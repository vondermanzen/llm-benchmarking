def gauss_elimination_gf2(matrix):
    lead = 0
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        
        matrix[i], matrix[r] = matrix[r], matrix[i]
        for j in range(rowCount):
            if j != r:
                if matrix[j][lead] == 1:
                    matrix[j] = [(el1 + el2) % 2 for el1, el2 in zip(matrix[j], matrix[r])]
        lead += 1
    return matrix

def rank_matrix_gf2(matrix):
    ref_matrix = gauss_elimination_gf2(matrix)
    rank = 0
    for row in ref_matrix:
        if any(x == 1 for x in row):
            rank += 1
    return rank

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    print(rank_matrix_gf2(matrix))