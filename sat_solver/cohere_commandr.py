def solve_sat(n, m, clauses):
    # Initialize an assignment with all variables as False (0)
    assignment = [0] * n

    # Function to flip the value of a variable in the assignment
    def flip(var):
        assignment[var - 1] = 1 - assignment[var - 1]

    # Try all possible assignments
    for i in range(2**n):
        # Convert the binary representation of i to a list of integers
        binary_i = [int(digit) for digit in bin(i)[2:].zfill(n)]

        # Update the assignment with the current binary representation
        for j in range(n):
            assignment[j] = binary_i[j]

        # Check if the current assignment satisfies all clauses
        if all(any(var in clause or -var in clause for var in range(1, n + 1)) for clause in clauses):
            return "SAT\n" + " ".join(map(str, assignment))

    return "UNSAT"


# Read input
n, m = map(int, input().split())
clauses = []
for _ in range(m):
    clauses.append(list(map(int, input().split())))

# Solve the SAT problem
print(solve_sat(n, m, clauses))