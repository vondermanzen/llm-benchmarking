# Script to sort a list of integers in ascending order from standard input

# Read a line of input, split into integers
numbers = list(map(int, input().split()))

# Sort the numbers
numbers.sort()

# Print the sorted list, space-separated
print(' '.join(map(str, numbers)))