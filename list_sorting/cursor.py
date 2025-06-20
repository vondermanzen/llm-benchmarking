# Read a line of input, split into integers
numbers = list(map(int, input().split()))
# Sort the list
numbers.sort()
# Print the sorted numbers, space-separated
print(' '.join(map(str, numbers)))
