def scc(graph):
    # Initialize the result and the index of the current vertex
    n = len(graph)
    result = [-1] * n
    index = [-1] * n
    for i in range(n):
        if result[i] == -1:
            # Initialize the index of the current vertex
            # and mark it as not visited
            result[i] = i
            index[i] = i
        else:
            # Find the lowest index of the strongly connected
            # component containing the current vertex
            low = result[index[i]]
            while True:
                # If the current vertex is in the same SCC
                # as before, we have a loop
                if low == i:
                    return len(set(result[:index[low]]))
                low = result[graph[low][1]]
            return len(set(result[:index[low]]))

# Test the function
n = 4
m = 4
graph = [[1, 2], [2, 3], [3, 1], [4, 1]]
print(scc(graph)) # Output: 2