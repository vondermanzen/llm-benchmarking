def gauss_elimination(matrix):
    lead = 0
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return matrix
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return matrix
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [ miv % 2 for miv in matrix[r]]
        for i in range(rowCount):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for iv, rv in zip(matrix[i], matrix[r])]
                matrix[i] = [miv % 2 for miv in matrix[i]]
        lead += 1
    return matrix

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
rank = sum(1 for row in gauss_elimination(matrix) if any(i != 0 for i in row))
print(rank)