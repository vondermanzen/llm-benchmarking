import sys

def solve_sat():
    """
    Main function to read CNF formula from stdin and find a satisfying assignment.
    """
    try:
        # Read problem dimensions: N variables, M clauses
        first_line = sys.stdin.readline().strip().split()
        if not first_line:
            # Handle empty input
            print("UNSAT")
            return
        N, M = map(int, first_line)

        # Read all clauses
        clauses = []
        for _ in range(M):
            clause = list(map(int, sys.stdin.readline().strip().split()))
            clauses.append(clause[:-1]) # Remove the trailing 0
    except (IOError, ValueError):
        # Handle cases of malformed input during reading
        print("UNSAT")
        return

    # assignment[i] will hold the boolean value for variable i (1-indexed)
    assignment = [None] * (N + 1)

    def check_clauses(current_assignment):
        """
        Check if the current partial assignment falsifies any clauses.
        A clause is falsified only if all its literals are assigned and evaluate to false.
        """
        for clause in clauses:
            is_clause_satisfied = False
            is_clause_unresolved = False

            for literal in clause:
                var = abs(literal)
                val = current_assignment[var]

                if val is None:
                    is_clause_unresolved = True
                    continue

                if (literal > 0 and val is True) or (literal < 0 and val is False):
                    is_clause_satisfied = True
                    break
            
            # If a clause is not satisfied and has no unassigned variables,
            # then this path is invalid.
            if not is_clause_satisfied and not is_clause_unresolved:
                return False
        return True

    def backtrack(var_index):
        """
        The core backtracking algorithm.
        """
        if var_index > N:
            # All variables assigned, a solution is found
            return assignment

        # Try assigning True to the current variable
        assignment[var_index] = True
        if check_clauses(assignment):
            result = backtrack(var_index + 1)
            if result:
                return result

        # If True didn't work, try assigning False
        assignment[var_index] = False
        if check_clauses(assignment):
            result = backtrack(var_index + 1)
            if result:
                return result
        
        # Backtrack: reset the variable assignment and return failure
        assignment[var_index] = None
        return None

    solution_assignment = backtrack(1)

    if solution_assignment:
        print("SAT")
        # Convert True/False to 1/0 for the output
        final_values = [str(int(val)) for val in solution_assignment[1:]]
        print(" ".join(final_values))
    else:
        print("UNSAT")

if __name__ == "__main__":
    solve_sat()