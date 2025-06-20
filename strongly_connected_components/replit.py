#!/usr/bin/env python3
"""
Strongly Connected Components Counter using Kosaraju's Algorithm

This program efficiently counts the number of strongly connected components (SCCs)
in a directed graph using Kosaraju's algorithm with O(V + E) time complexity.

Author: Generated for SCC counting task
Date: June 20, 2025
"""

import sys
from collections import defaultdict


class SCCCounter:
    """
    A class to count strongly connected components in a directed graph
    using Kosaraju's algorithm.
    """
    
    def __init__(self, n):
        """
        Initialize the SCC counter for a graph with n vertices.
        
        Args:
            n (int): Number of vertices in the graph (1-indexed)
        """
        self.n = n
        # Adjacency list for original graph
        self.graph = defaultdict(list)
        # Adjacency list for transpose graph
        self.transpose = defaultdict(list)
        # Track visited vertices
        self.visited = [False] * (n + 1)
        # Stack to store vertices by finishing time
        self.finish_stack = []
    
    def add_edge(self, u, v):
        """
        Add a directed edge from vertex u to vertex v.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
        """
        self.graph[u].append(v)
        self.transpose[v].append(u)  # Add reverse edge to transpose
    
    def dfs_first_pass(self, vertex):
        """
        First DFS pass to fill the stack with vertices in order of finishing time.
        
        Args:
            vertex (int): Current vertex being processed
        """
        self.visited[vertex] = True
        
        # Visit all adjacent vertices
        for neighbor in self.graph[vertex]:
            if not self.visited[neighbor]:
                self.dfs_first_pass(neighbor)
        
        # Add to stack when done processing (finishing time)
        self.finish_stack.append(vertex)
    
    def dfs_second_pass(self, vertex):
        """
        Second DFS pass on transpose graph to identify one SCC.
        
        Args:
            vertex (int): Current vertex being processed
        """
        self.visited[vertex] = True
        
        # Visit all adjacent vertices in transpose graph
        for neighbor in self.transpose[vertex]:
            if not self.visited[neighbor]:
                self.dfs_second_pass(neighbor)
    
    def count_sccs(self):
        """
        Count the number of strongly connected components using Kosaraju's algorithm.
        
        Returns:
            int: Number of strongly connected components
        """
        # Step 1: Fill vertices in stack according to their finishing times
        # Reset visited array
        self.visited = [False] * (self.n + 1)
        
        for vertex in range(1, self.n + 1):
            if not self.visited[vertex]:
                self.dfs_first_pass(vertex)
        
        # Step 2: Process vertices from stack (in reverse finishing time order)
        # and count SCCs in transpose graph
        self.visited = [False] * (self.n + 1)
        scc_count = 0
        
        while self.finish_stack:
            vertex = self.finish_stack.pop()
            if not self.visited[vertex]:
                # Found a new SCC
                self.dfs_second_pass(vertex)
                scc_count += 1
        
        return scc_count


def read_input():
    """
    Read input from standard input according to the specified format.
    
    Returns:
        tuple: (n, edges) where n is number of vertices and edges is list of (u, v) pairs
    """
    try:
        # Read first line with N and M
        line = input().strip()
        n, m = map(int, line.split())
        
        # Validate input constraints
        if not (1 <= n <= 10000):
            raise ValueError(f"Number of vertices {n} out of range [1, 10000]")
        if not (0 <= m <= 100000):
            raise ValueError(f"Number of edges {m} out of range [0, 100000]")
        
        edges = []
        
        # Read M edges
        for i in range(m):
            line = input().strip()
            if not line:
                raise ValueError(f"Missing edge on line {i + 2}")
            
            u, v = map(int, line.split())
            
            # Validate vertex indices
            if not (1 <= u <= n) or not (1 <= v <= n):
                raise ValueError(f"Edge ({u}, {v}) contains invalid vertex indices")
            
            edges.append((u, v))
        
        return n, edges
    
    except EOFError:
        raise ValueError("Unexpected end of input")
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Invalid input format: expected integers")
        raise


def main():
    """
    Main function to execute the SCC counting program.
    """
    try:
        # Read input
        n, edges = read_input()
        
        # Handle empty graph case
        if n == 0:
            print(0)
            return
        
        # Create SCC counter and add edges
        scc_counter = SCCCounter(n)
        
        # Add all edges (handles self-loops and multiple edges automatically)
        for u, v in edges:
            scc_counter.add_edge(u, v)
        
        # Count and output SCCs
        result = scc_counter.count_sccs()
        print(result)
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
