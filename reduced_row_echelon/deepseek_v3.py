def gf2_rank(N, M, equations):
    rank = 0
    for col in range(M + 1):
        # Find a row with a leading 1 in the current column
        pivot = -1
        for row in range(rank, N):
            if equations[row][col] == 1:
                pivot = row
                break
        if pivot == -1:
            continue
        
        # Swap the current row with the pivot row
        equations[rank], equations[pivot] = equations[pivot], equations[rank]
        
        # Eliminate this column in all other rows
        for row in range(N):
            if row != rank and equations[row][col] == 1:
                equations[row] = [(x + y) % 2 for x, y in zip(equations[row], equations[rank])]
        
        rank += 1
    return rank

# Read input
N, M = map(int, input().split())
equations = []
for _ in range(N):
    row = list(map(int, input().split()))
    equations.append(row)

# Compute rank
rank = gf2_rank(N, M, equations)
print(rank)