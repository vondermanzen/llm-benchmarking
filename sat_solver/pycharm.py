def solve_sat(num_vars, clauses):
    """
    Solve the SAT problem using the DPLL algorithm.

    Args:
        num_vars (int): Number of variables.
        clauses (list): List of clauses, where each clause is a list of literals.

    Returns:
        list or None: A satisfying assignment if the formula is satisfiable,
                     None otherwise.
    """
    # Initialize assignment with None for each variable (unassigned)
    # We use 1-based indexing for variables as specified in the problem
    assignment = [None] * (num_vars + 1)  # +1 because vars are 1-indexed

    def is_clause_satisfied(clause, current_assignment):
        """
        Check if a clause is satisfied by the current assignment.

        Args:
            clause: A list of literals.
            current_assignment: Current variable assignments.

        Returns:
            bool: True if the clause is satisfied, False otherwise.
        """
        for literal in clause:
            var = abs(literal)
            if current_assignment[var] is not None:
                # If literal is positive and var is True, or
                # if literal is negative and var is False
                if (literal > 0 and current_assignment[var] == 1) or \
                   (literal < 0 and current_assignment[var] == 0):
                    return True
        return False

    def is_formula_satisfied(current_clauses, current_assignment):
        """
        Check if all clauses are satisfied by the current assignment.

        Args:
            current_clauses: List of clauses.
            current_assignment: Current variable assignments.

        Returns:
            bool: True if all clauses are satisfied, False otherwise.
        """
        for clause in current_clauses:
            if not is_clause_satisfied(clause, current_assignment):
                return False
        return True

    def unit_propagation(current_clauses, current_assignment):
        """
        Apply unit propagation to simplify the formula.

        Args:
            current_clauses: List of clauses.
            current_assignment: Current variable assignments.

        Returns:
            tuple: (updated_clauses, updated_assignment, status)
                  status is 'SAT' if formula is satisfied, 'UNSAT' if unsatisfiable,
                  'CONTINUE' if more work needed.
        """
        updated_clauses = []
        changes_made = True

        while changes_made:
            changes_made = False

            # Check for empty clauses (unsatisfiable)
            for clause in current_clauses:
                unsatisfied_literals = 0
                for literal in clause:
                    var = abs(literal)
                    if current_assignment[var] is None or \
                       (literal > 0 and current_assignment[var] == 1) or \
                       (literal < 0 and current_assignment[var] == 0):
                        unsatisfied_literals += 1
                if unsatisfied_literals == 0:
                    return current_clauses, current_assignment, 'UNSAT'

            # Look for unit clauses
            for clause in current_clauses:
                # Skip clauses that are already satisfied
                if is_clause_satisfied(clause, current_assignment):
                    continue

                # Find unassigned literals in this clause
                unassigned_literals = [lit for lit in clause if current_assignment[abs(lit)] is None]

                # If only one unassigned literal, it must be True to satisfy clause
                if len(unassigned_literals) == 1:
                    literal = unassigned_literals[0]
                    var = abs(literal)
                    # Assign value to make literal True
                    current_assignment[var] = 1 if literal > 0 else 0
                    changes_made = True

            # Simplify clauses based on current assignment
            updated_clauses = []
            for clause in current_clauses:
                # Skip clauses that are already satisfied
                if is_clause_satisfied(clause, current_assignment):
                    continue

                # Keep only unassigned literals or literals that could be True
                new_clause = []
                for literal in clause:
                    var = abs(literal)
                    if current_assignment[var] is None or \
                       (literal > 0 and current_assignment[var] == 1) or \
                       (literal < 0 and current_assignment[var] == 0):
                        new_clause.append(literal)

                if new_clause:
                    updated_clauses.append(new_clause)
                else:
                    # Empty clause means this branch is unsatisfiable
                    return current_clauses, current_assignment, 'UNSAT'

            current_clauses = updated_clauses

            # Check if all clauses are satisfied
            if not current_clauses:
                return current_clauses, current_assignment, 'SAT'

        return current_clauses, current_assignment, 'CONTINUE'

    def dpll(current_clauses, current_assignment):
        """
        Recursive DPLL algorithm to find a satisfying assignment.

        Args:
            current_clauses: List of clauses.
            current_assignment: Current variable assignments.

        Returns:
            list or None: A satisfying assignment if found, None otherwise.
        """
        # Apply unit propagation
        current_clauses, current_assignment, status = unit_propagation(current_clauses, current_assignment)

        if status == 'SAT':
            return current_assignment
        elif status == 'UNSAT':
            return None

        # Choose an unassigned variable
        for var in range(1, num_vars + 1):
            if current_assignment[var] is None:
                # Try setting the variable to True (1)
                current_assignment[var] = 1
                result = dpll(current_clauses, current_assignment.copy())
                if result is not None:
                    return result

                # Try setting the variable to False (0)
                current_assignment[var] = 0
                result = dpll(current_clauses, current_assignment.copy())
                if result is not None:
                    return result

                # Both assignments failed, backtrack
                current_assignment[var] = None
                return None

        # All variables assigned and no conflicts
        return current_assignment

    # Start DPLL algorithm
    result = dpll(clauses, assignment)
    return result

def main():
    # Read input
    n, m = map(int, input().split())

    # Read clauses
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        # Remove the trailing 0 and add the clause
        clauses.append(clause[:-1])

    # Solve the SAT problem
    assignment = solve_sat(n, clauses)

    # Output the result
    if assignment is None:
        print("UNSAT")
    else:
        print("SAT")
        # Convert to 0/1 list and skip the 0th element (1-indexed variables)
        result = []
        for i in range(1, n + 1):
            # If a variable wasn't assigned, arbitrarily set it to 0
            result.append(1 if assignment[i] == 1 else 0)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
