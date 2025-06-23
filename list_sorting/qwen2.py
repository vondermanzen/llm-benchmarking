# Read a list of integers from standard input
numbers = list(map(int, input().split()))

# Sort the list of integers in ascending order
numbers.sort()

# Print the sorted list to standard output
print(' '.join(map(str, numbers)))