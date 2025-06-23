Okay, I need to solve this SAT problem where I have to find a satisfying assignment for a given CNF formula. Let's think about how to approach this.

First, the input format: the first line has N variables and M clauses. Then each clause is a list of integers ending with 0. Each non-zero integer represents a variable or its negation. So, for example, 1 is x1, -2 is not x2, etc.

The output should be either SAT followed by the assignments or UNSAT if impossible.

Hmm, the problem is to find any satisfying assignment. Since N is up to 20, maybe a brute-force approach is feasible here. Because 2^20 is about a million, which is manageable. Wait, 2^20 is 1,048,576. That's way too big. Oh wait, but maybe the code can be optimized. Wait, but 20 variables, each can be 0 or 1. So total possible assignments are 2^20, which is over a million. That's a lot, but maybe for the problem constraints, it's manageable. Let's see. For each possible assignment, check all clauses. If any assignment satisfies all clauses, return it. Otherwise, UNSAT.

But generating all possible assignments might be time-consuming. Let's think: how many possible assignments are there? For N=20, 2^20 is about a million. For each assignment, we need to check M clauses. Each clause can have up to N variables (since variables are 1 to N). For each clause, check if at least one literal in the clause is true under the assignment.

So the steps would be:

1. Read N and M.
2. Read each clause, stripping the trailing 0.
3. Generate all possible assignments (each variable is 0 or 1).
4. For each assignment, check all clauses. If all are satisfied, output the assignment.
5. If none found after all, output UNSAT.

But how to generate all possible assignments efficiently in Python?

In Python, for N variables, we can generate all possible tuples of 0s and 1s. For example, using itertools.product.

But for N=20, each assignment is a tuple of length 20. So for each possible combination in product([0,1], repeat=N), check if it satisfies all clauses.

Yes. So the code can be structured as follows:

- Read N and M.
- Read M clauses. For each clause, process the list (excluding the trailing 0). For example, the first example input has clauses [1,2,0] and [-1,-2,3,0]. So the actual literals are [1,2] and [-1,-2,3].

Then, for each possible assignment (a list or tuple of 0s and 1s), check each clause. For a clause, check if at least one literal in the clause is satisfied by the assignment.

How to check a clause? For a literal in the clause, the variable is abs(literal). The value in the assignment is assignment[variable-1] (since variables are 1-based). The literal is positive if the value is 1, negative if the value is 0.

So for a literal x in the clause:

if x > 0: then check if assignment[var-1] is 1.

if x < 0: check if assignment[var-1] is 0.

So for each clause, iterate through its literals. If any of them is true, the clause is satisfied.

Once an assignment is found that satisfies all clauses, output "SAT" followed by the assignment.

If after checking all possible assignments none satisfy all clauses, output "UNSAT".

Now, the code.

First, read N and M.

Then read M lines. For each line, split into integers, then slice off the last element (the 0). So for example, the first line in example 1 is 1 2 0 → [1,2]. The second line is -1 -2 3 0 → [-1,-2,3].

Then, generate all possible assignments. For each assignment in itertools.product([0,1], repeat=N):

Check each clause. For each clause, check if any literal in the clause is satisfied.

If all clauses are satisfied, then output the assignment.

But how to handle the order of variables? The output requires the variables 1 to N in order. So the assignment tuple should be for variables 1 to N. So for example, if the assignment is (1,0,1), then variable 1 is 1 (True), variable 2 is 0 (False), variable 3 is 1 (True).

So the code can loop through all possible assignments in order, and for each, check all clauses.

Now, code steps:

Import itertools.

Read N, M.

clauses = []
for _ in range(M):
    line = list(map(int, input().split()))
    clause = line[:-1]  # remove the trailing 0
    clauses.append(clause)

for assignment in itertools.product([0,1], repeat=N):
    all_satisfied = True
    for clause in clauses:
        clause_satisfied = False
        for lit in clause:
            var = abs(lit)
            val = assignment[var-1]
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                clause_satisfied = True
                break
        if not clause_satisfied:
            all_satisfied = False
            break
    if all_satisfied:
        print("SAT")
        print(' '.join(map(str, assignment)))
        exit()

print("UNSAT")

Wait, but in the example input 1, the output is "1 0 1", which is the assignment for variables 1, 2, 3. So the code's assignment is a tuple in the order of variables 1 to N. So the code should output the assignment in the correct order, which it does.

But wait, in the code, the assignment is generated as a tuple where the first element is the value of variable 1, the second of variable 2, etc. So when we print ' '.join(map(str, assignment)), that's correct.

Testing the first example:

Variables 1,2,3.

The assignment (1,0,1) would be True, False, True.

Check the first clause [1,2]. The literals are 1 (var 1 is 1 → True) and 2 (var 2 is 0 → False). So one of them is True. So clause is satisfied.

Second clause [-1, -2, 3]. Literals are -1 (var 1 is 1 → False), -2 (var 2 is 0 → True), 3 (var 3 is 1 → True). So at least one is True. So clause is satisfied.

So the code would output SAT and 1 0 1.

Which matches the example.

For the second example:

Input is 2 variables, 3 clauses.

Clauses:

1 → [1]

-1 → [-1]

2 -2 → [2,-2]

So the clauses are:

( x1 ) ∧ ( ¬x1 ) ∧ ( x2 ∨ ¬x2 )

This is unsatisfiable. So the code would check all possible assignments (4 possibilities):

(0,0): check clauses.

First clause: x1 is 0 → no. So clause not satisfied.

(0,1):

First clause: x1 is 0 → no. So clause not satisfied.

(1,0):

First clause: x1 is 1 → yes. Second clause: x1 is 1 → but clause requires ¬x1 → 0. So second clause not satisfied.

(1,1):

First clause: x1 is 1 → yes. Second clause: ¬x1 is 0 → no. So second clause not satisfied.

So all assignments result in at least one clause not being satisfied. So code outputs UNSAT.

Which is correct.

So the code seems to handle these cases.

But what about the order of checking assignments? The code checks all possible assignments in the order generated by itertools.product. Since the problem allows any satisfying assignment, the first one found is printed.

The code is correct.

But for N=20, itertools.product would generate 2^20 = 1,048,576 assignments. Each assignment requires checking M clauses, each clause up to N literals. So for M=100 and N=20, each assignment check is O(M*N) operations. For 1e6 * 1e4 (if M*N is 1e4), that's 1e10 operations, which is way too slow. Oh wait, but M is up to 100 and N up to 20. So M*N is up to 2000. So per assignment, 2000 operations. For 1e6 assignments, that's 2e9 operations. That's way too slow for Python.

Wait, this is a problem. For N=20, the code would take 2^20 * M * N steps. For M=100, N=20, that's 1