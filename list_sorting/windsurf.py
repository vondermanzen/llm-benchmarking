# Read input as a single line and split into list
numbers = list(map(int, input().split()))

# Sort the list
numbers.sort()

# Print sorted numbers with spaces
print(' '.join(map(str, numbers)))
