from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.transpose = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.transpose[v].append(u)
    
    def fill_order(self, v, visited, stack):
        visited[v] = True
        
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        
        stack.append(v)
    
    def dfs(self, v, visited):
        visited[v] = True
        
        for i in self.transpose[v]:
            if not visited[i]:
                self.dfs(i, visited)
    
    def count_scc(self):
        visited = [False] * (self.V + 1)
        stack = []
        
        # First DFS to fill the stack
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.fill_order(i, visited, stack)
        
        # Reset visited array for second DFS
        visited = [False] * (self.V + 1)
        
        # Count SCCs using second DFS
        scc_count = 0
        while stack:
            i = stack.pop()
            if not visited[i]:
                self.dfs(i, visited)
                scc_count += 1
        
        return scc_count

def main():
    try:
        # Read number of vertices and edges
        N, M = map(int, input().strip().split())
        
        # Validate input constraints
        if not (1 <= N <= 10000):
            print("Number of vertices must be between 1 and 10000")
            return
        if not (0 <= M <= 100000):
            print("Number of edges must be between 0 and 100000")
            return
        
        # Create graph
        g = Graph(N)
        
        # Read edges
        for _ in range(M):
            u, v = map(int, input().strip().split())
            
            # Validate vertex numbers
            if not (1 <= u <= N and 1 <= v <= N):
                print("Vertex numbers must be between 1 and N")
                return
            
            g.add_edge(u, v)
        
        # Print number of SCCs
        print(g.count_scc())
        
    except ValueError:
        print("Invalid input format")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
