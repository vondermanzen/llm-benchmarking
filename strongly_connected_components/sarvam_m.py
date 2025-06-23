First, I remember that the standard algorithm for finding SCCs in a directed graph is Kosaraju's algorithm. It's efficient enough for the given constraints. The steps are roughly: perform a DFS on the original graph and record the finishing times of the nodes. Then reverse all the edges of the graph and process the nodes in the order of decreasing finishing times. Each tree in the DFS forest of this reversed graph is an SCC. The count of these trees is the answer.

So, the plan is:

1. Read the graph and build the adjacency list.
2. Perform the first pass of DFS to get the finishing times.
3. Reverse the graph.
4. Perform DFS on the reversed graph in the order of decreasing finishing times.
5. Count the number of DFS trees in the second pass, which is the number of SCCs.

Let me think about the steps in code.

First, read N and M. Then read M edges and build the adjacency list. Also, create a reversed adjacency list for step 3.

Wait, for the original graph and the reversed graph. So for each edge u -> v, the original adjacency list adds v to u's list, and the reversed adds u to v's list.

Then, the first DFS. We need to track visited nodes and the order of finishing. So, during the first DFS, we push nodes onto a stack (or list) in finishing order. The order is such that the last node visited (the one that finishes first) comes first in the stack.

Wait, Kosaraju's algorithm uses the finishing times in reverse order. So after the first DFS, the nodes are processed in the order of their finishing times, which is from last to first. So the stack will be [n, n-1, ..., 1] if the original order was 1 to n.

So, the first step is to perform a standard DFS and collect the finishing times in a list. Then, we sort the nodes in the order of their finishing times (from last to first) and process them in that order for the second DFS on the reversed graph.

Wait, no. The nodes are processed in the order of their finishing times, which is the order in which they were finished in the first pass. So the first node in the stack is the last one finished. So when we process them in reverse order of the stack, we start with the last finished node.

So, for example, if the finishing order is [3, 2, 1], then the stack is [3,2,1], and we process them in reverse order (1,2,3), but that's not right. Wait, no. Wait, the first DFS finishes nodes in the order they are done. So the first node to finish is the one that is pushed first. So the stack is built in the order of finishing, which is the reverse order of processing. So the order of the stack is [u, v, w] if u is finished first, then v, then w. So when we process them in the order of the stack, it's u, v, w. But in Kosaraju's algorithm, we process them in the reverse order of their finishing times. So the nodes are processed in the order of decreasing finishing times. So the stack is [u, v, w], and we process them in reverse order (w, v, u). So the processing order is the reverse of the stack.

So, for the second DFS, we take the nodes in the order of their finishing times, which is the reverse of the stack. So the stack is built by appending as each node is finished. So the stack is in the order of finishing. So to process in reverse order, we can iterate from the end to the start of the stack.

So, in code:

First, perform a DFS, and for each node, when it's finished, append it to a list (stack). Then, the processing order for the reversed graph is in reverse of this stack.

Wait, no. Let's see. Suppose during the first DFS, the nodes are visited in the order A, B, C, D. Suppose A is processed first, then B, then C, then D. The finishing order is D, C, B, A. So the stack would be [D, C, B, A]. Then, the processing order for the reversed graph is D, C, B, A. So for each node in the stack, in order, we process them. But in the reversed graph, if a node is in the same SCC as others, processing them in this order would group them together.

So, the code steps:

1. Read N and M.

2. Build original adjacency list and reversed adjacency list.

3. Perform first DFS, track visited, and collect the finishing order.

4. Initialize a visited array for the reversed graph.

5. Iterate through the stack in order (from last to first), i.e., the order of finishing times. For each node, if not visited, perform DFS on the reversed graph, incrementing the count each time.

So, the code outline:

import sys
sys.setrecursionlimit(1 << 25)  # To handle large recursion depth if necessary, but better to iterate.

n, m = map(int, sys.stdin.readline().split())

if m == 0:
    print(n)
    exit()

adj = [[] for _ in range(n+1)]
rev_adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    rev_adj[v].append(u)

visited = [False]*(n+1)
order = []

def dfs(u):
    stack = [(u, False)]
    while stack:
        node, processed = stack.pop()
        if not processed:
            if visited[node]:
                continue
            visited[node] = True
            stack.append( (node, True) )
            for v in adj[node]:
                if not visited[v]:
                    stack.append( (v, False) )
        else:
            order.append(node)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

visited_rev = [False]*(n+1)
count = 0

for node in reversed(order):
    if not visited_rev[node]:
        stack = [node]
        visited_rev[node] = True
        while stack:
            u = stack.pop()
            for v in rev_adj[u]:
                if not visited_rev[v]:
                    visited_rev[v] = True
                    stack.append(v)
        count +=1

print(count)

Wait, but in the code above, the first DFS is implemented iteratively using a stack. That's better for handling large graphs to avoid recursion depth issues. So for the first DFS, we use an iterative approach.

Then, the order is collected in the order of finishing. Then, we process the nodes in reversed(order), which is the correct order for the second pass.

In the second pass, for each node in reversed(order), if not visited, we perform a DFS (iteratively again) on the reversed adjacency list. Each such DFS corresponds to an SCC.

This should work.

Testing the example input:

4 4

1 2

2 3

3 1

4 1

The original adj:

1: [2]

2: [3]

3: [1]

4: [1]

rev_adj:

1: [1,4]

2: [2]

3: [3]

4: [4]

First DFS:

Start with 1. Process 1, mark as visited. Then stack appends 2, then 3, then finish 3 (order becomes [3]), then process 2 (after 3 is done, append 2 to order (now [3,2]), then process 1, append 1 (order [3,2,1]). Then, process 4. Since 4 is not visited, mark as visited, stack appends 1 (but 1 is already visited). So order becomes [3,2,1,4].

Then reversed(order) is [4,1,2,3].

Processing 4: not visited_rev. Process it. rev_adj[4] is [4]. So stack is [4], mark as visited. Process 4, look at rev_adj[4] (4), which is already visited. So count becomes 1.

Next node is 1: not visited_rev. Process it. rev_adj[1] is [1,4]. 4 is visited. So stack starts with 1. Mark as visited. Then look at rev_adj[1] entries. 1 is already visited. So after popping 1, no more nodes. count becomes 2.

Then process 2: not visited. rev_adj[2] is [2]. stack [2], mark as visited. Then look at rev_adj[2] entries (2 is processed). count becomes 3.

Then process 3: rev_adj[3] is [3]. stack [3], mark as visited. count becomes 4.

So total count is 4. But the example output is 2. Wait, this is a problem.

Wait, the example input's correct output is 2. But according to this