#!/usr/bin/env python3
"""
SAT Solver - Boolean Satisfiability Problem Solver
Implements a backtracking algorithm with constraint propagation
to solve Boolean formulas in Conjunctive Normal Form (CNF).
"""

import sys
from typing import List, Dict, Optional, Tuple, Set


class SATSolver:
    """
    SAT Solver using backtracking with boolean constraint propagation.
    """
    
    def __init__(self, num_variables: int, clauses: List[List[int]]):
        """
        Initialize the SAT solver.
        
        Args:
            num_variables: Number of boolean variables (1 to N)
            clauses: List of clauses, each clause is a list of literals
        """
        self.num_variables = num_variables
        self.clauses = clauses
        self.assignment = {}  # Variable assignments: variable -> True/False
        self.decision_level = 0
        
    def is_clause_satisfied(self, clause: List[int]) -> bool:
        """
        Check if a clause is satisfied by current assignment.
        
        Args:
            clause: List of literals in the clause
            
        Returns:
            True if clause is satisfied, False otherwise
        """
        for literal in clause:
            var = abs(literal)
            if var in self.assignment:
                # Positive literal: satisfied if variable is True
                # Negative literal: satisfied if variable is False
                if (literal > 0 and self.assignment[var]) or \
                   (literal < 0 and not self.assignment[var]):
                    return True
        return False
    
    def is_clause_unit(self, clause: List[int]) -> Optional[int]:
        """
        Check if a clause is a unit clause (only one unassigned literal).
        
        Args:
            clause: List of literals in the clause
            
        Returns:
            The unassigned literal if it's a unit clause, None otherwise
        """
        unassigned_literals = []
        
        for literal in clause:
            var = abs(literal)
            if var not in self.assignment:
                unassigned_literals.append(literal)
            elif (literal > 0 and self.assignment[var]) or \
                 (literal < 0 and not self.assignment[var]):
                # Clause is already satisfied
                return None
        
        # Unit clause has exactly one unassigned literal
        if len(unassigned_literals) == 1:
            return unassigned_literals[0]
        
        return None
    
    def is_clause_conflicted(self, clause: List[int]) -> bool:
        """
        Check if a clause is conflicted (all literals are false).
        
        Args:
            clause: List of literals in the clause
            
        Returns:
            True if clause is conflicted, False otherwise
        """
        for literal in clause:
            var = abs(literal)
            if var not in self.assignment:
                return False
            if (literal > 0 and self.assignment[var]) or \
               (literal < 0 and not self.assignment[var]):
                return False
        return True
    
    def unit_propagation(self) -> bool:
        """
        Perform unit propagation: if a clause has only one unassigned literal,
        assign it the value that satisfies the clause.
        
        Returns:
            False if a conflict is detected, True otherwise
        """
        changed = True
        while changed:
            changed = False
            
            for clause in self.clauses:
                # Skip satisfied clauses
                if self.is_clause_satisfied(clause):
                    continue
                
                # Check for conflicts
                if self.is_clause_conflicted(clause):
                    return False
                
                # Check for unit clauses
                unit_literal = self.is_clause_unit(clause)
                if unit_literal is not None:
                    var = abs(unit_literal)
                    value = unit_literal > 0
                    
                    if var not in self.assignment:
                        self.assignment[var] = value
                        changed = True
        
        return True
    
    def find_pure_literals(self) -> Dict[int, bool]:
        """
        Find pure literals (variables that appear only positively or only negatively).
        
        Returns:
            Dictionary mapping pure literal variables to their values
        """
        literal_polarities = {}  # variable -> set of polarities (True, False)
        
        for clause in self.clauses:
            # Skip satisfied clauses
            if self.is_clause_satisfied(clause):
                continue
                
            for literal in clause:
                var = abs(literal)
                if var not in self.assignment:
                    if var not in literal_polarities:
                        literal_polarities[var] = set()
                    literal_polarities[var].add(literal > 0)
        
        pure_literals = {}
        for var, polarities in literal_polarities.items():
            if len(polarities) == 1:
                # Pure literal: appears only positively or only negatively
                pure_literals[var] = list(polarities)[0]
        
        return pure_literals
    
    def choose_variable(self) -> Optional[int]:
        """
        Choose the next unassigned variable for branching.
        Uses a simple heuristic: choose the variable that appears in most unsatisfied clauses.
        
        Returns:
            Variable number to assign next, or None if all variables are assigned
        """
        variable_counts = {}
        
        for clause in self.clauses:
            if not self.is_clause_satisfied(clause):
                for literal in clause:
                    var = abs(literal)
                    if var not in self.assignment:
                        variable_counts[var] = variable_counts.get(var, 0) + 1
        
        if not variable_counts:
            return None
        
        # Choose variable with highest count
        return max(variable_counts.keys(), key=lambda v: variable_counts[v])
    
    def all_clauses_satisfied(self) -> bool:
        """
        Check if all clauses are satisfied by current assignment.
        
        Returns:
            True if all clauses are satisfied, False otherwise
        """
        for clause in self.clauses:
            if not self.is_clause_satisfied(clause):
                return False
        return True
    
    def solve_recursive(self) -> bool:
        """
        Recursive backtracking SAT solver with constraint propagation.
        
        Returns:
            True if satisfiable, False if unsatisfiable
        """
        # Unit propagation
        if not self.unit_propagation():
            return False
        
        # Pure literal elimination
        pure_literals = self.find_pure_literals()
        for var, value in pure_literals.items():
            self.assignment[var] = value
        
        # Check if all clauses are satisfied
        if self.all_clauses_satisfied():
            return True
        
        # Choose next variable to branch on
        var = self.choose_variable()
        if var is None:
            # All variables assigned but not all clauses satisfied
            return False
        
        # Try assigning True
        self.assignment[var] = True
        if self.solve_recursive():
            return True
        
        # Backtrack: try assigning False
        self.assignment[var] = False
        if self.solve_recursive():
            return True
        
        # Backtrack: unassign variable
        del self.assignment[var]
        return False
    
    def solve(self) -> Tuple[bool, Optional[List[int]]]:
        """
        Solve the SAT problem.
        
        Returns:
            Tuple of (is_satisfiable, assignment_list)
            assignment_list is None if unsatisfiable, otherwise list of 0/1 values
        """
        self.assignment = {}
        
        if self.solve_recursive():
            # Convert assignment to output format
            result = []
            for i in range(1, self.num_variables + 1):
                if i in self.assignment:
                    result.append(1 if self.assignment[i] else 0)
                else:
                    # Unassigned variables can be set to any value
                    result.append(0)
            return True, result
        else:
            return False, None


def parse_input() -> Tuple[int, List[List[int]]]:
    """
    Parse CNF input format from stdin.
    
    Returns:
        Tuple of (num_variables, clauses)
    """
    try:
        # Read first line: N (variables) and M (clauses)
        line = input().strip()
        n, m = map(int, line.split())
        
        if n < 1 or n > 20:
            raise ValueError(f"Number of variables must be between 1 and 20, got {n}")
        if m < 1 or m > 100:
            raise ValueError(f"Number of clauses must be between 1 and 100, got {m}")
        
        clauses = []
        
        # Read M clauses
        for i in range(m):
            line = input().strip()
            literals = list(map(int, line.split()))
            
            # Remove the trailing 0
            if not literals or literals[-1] != 0:
                raise ValueError(f"Clause {i+1} must end with 0")
            
            clause = literals[:-1]  # Remove the 0
            
            if not clause:
                raise ValueError(f"Clause {i+1} is empty")
            
            # Validate literal values
            for literal in clause:
                if literal == 0:
                    raise ValueError(f"Invalid literal 0 in clause {i+1}")
                if abs(literal) > n:
                    raise ValueError(f"Variable {abs(literal)} exceeds maximum {n} in clause {i+1}")
            
            clauses.append(clause)
        
        return n, clauses
        
    except EOFError:
        raise ValueError("Unexpected end of input")
    except ValueError as e:
        raise ValueError(f"Input parsing error: {e}")


def main():
    """
    Main function to run the SAT solver.
    """
    try:
        # Parse input
        num_variables, clauses = parse_input()
        
        # Create and run solver
        solver = SATSolver(num_variables, clauses)
        is_sat, assignment = solver.solve()
        
        # Output result
        if is_sat:
            print("SAT")
            print(" ".join(map(str, assignment)))
        else:
            print("UNSAT")
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nSolver interrupted", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
