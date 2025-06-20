import sys

# Read a line from standard input
input_line = sys.stdin.readline()

# Split the line into strings, convert to integers
numbers = list(map(int, input_line.strip().split()))

# Sort the list in ascending order
numbers.sort()

# Print the sorted numbers, space-separated
print(' '.join(map(str, numbers)))