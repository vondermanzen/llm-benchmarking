import sys

# It's good practice to set a higher recursion limit for graph problems
# as the default limit (often 1000) can be too low for deep traversal.
sys.setrecursionlimit(200000)

class Graph:
    """
    A class to represent a directed graph using an adjacency list.
    The graph is 0-indexed internally.
    """
    def __init__(self, vertices):
        self.V = vertices
        # Initialize an adjacency list for all vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        """Adds a directed edge from vertex u to vertex v."""
        if 0 <= u < self.V and 0 <= v < self.V:
            self.graph[u].append(v)

    def dfs1(self, v, visited, stack):
        """
        First pass of Depth First Search (DFS).
        This fills a stack with vertices based on their finishing times.
        A vertex is pushed to the stack only after all its descendants
        in the DFS tree have been processed.
        """
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs1(i, visited, stack)
        stack.append(v)

    def get_transpose(self):
        """
        Returns a new Graph object that is the transpose of this graph.
        The transpose of a graph has all its edges reversed.
        """
        g_rev = Graph(self.V)
        for i in range(self.V):
            for j in self.graph[i]:
                g_rev.add_edge(j, i)
        return g_rev

    def dfs2(self, v, visited, scc_nodes):
        """
        Second pass of DFS, performed on the transposed graph.
        This traversal finds all nodes belonging to a single SCC.
        """
        visited[v] = True
        scc_nodes.append(v + 1) # Store as 1-indexed for output
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs2(i, visited, scc_nodes)

    def find_sccs(self):
        """
        The main function that finds and returns the number of SCCs
        and a list of all SCCs using Kosaraju's algorithm.
        """
        stack = []
        visited = [False] * self.V
        
        # Step 1: Perform DFS on the original graph to get finishing times (in the stack)
        for i in range(self.V):
            if not visited[i]:
                self.dfs1(i, visited, stack)

        # Step 2: Get the transpose of the graph
        g_rev = self.get_transpose()

        # Step 3: Process vertices from the stack on the transposed graph
        visited = [False] * self.V
        scc_count = 0
        all_sccs = []
        while stack:
            v = stack.pop()
            if not visited[v]:
                scc_nodes = []
                g_rev.dfs2(v, visited, scc_nodes)
                all_sccs.append(scc_nodes)
                scc_count += 1
        
        return scc_count, all_sccs

def solve_from_string(graph_input_str):
    """
    Parses graph input from a string, builds the graph, and finds SCCs.
    """
    lines = graph_input_str.strip().split('\n')
    
    if not lines or not lines[0].strip():
        print("Error: Input is empty.")
        return 0, []

    # Parse the number of vertices and edges from the first line
    try:
        num_vertices, num_edges = map(int, lines[0].split())
    except (ValueError, IndexError):
        print(f"Error: Invalid first line: '{lines[0]}'. Expected 'num_vertices num_edges'.")
        return 0, []

    g = Graph(num_vertices)
    
    # Parse edges from the subsequent lines
    edge_count = 0
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        try:
            u, v = map(int, line.split())
            # The algorithm uses 0-based indexing for vertices, so subtract 1
            g.add_edge(u - 1, v - 1)
            edge_count += 1
        except (ValueError, IndexError):
            print(f"Warning: Skipping invalid edge line: '{line}'")
    
    if edge_count != num_edges:
        print(f"Warning: Expected {num_edges} edges based on the first line, but found {edge_count} valid edges.")

    scc_count, all_sccs = g.find_sccs()
    return scc_count, all_sccs

# --- Execution ---
# The graph representation is passed in from the application.
# This example uses the default input graph.
graph_representation = """4 4
1 2
2 3
3 1
4 1"""

scc_count, all_sccs = solve_from_string(graph_representation)

print(f"Number of Strongly Connected Components: {scc_count}")
# You can uncomment the lines below to also print the nodes in each SCC
# print("\nStrongly Connected Components:")
# for i, scc in enumerate(all_sccs):
#     print(f"  SCC {i + 1}: {scc}")