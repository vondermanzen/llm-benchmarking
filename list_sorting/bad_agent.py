import sys

# Read a line of input from standard input
input_line = sys.stdin.readline()

# Split the input string into a list of integers
numbers = list(map(int, input_line.strip().split()))

# Print the sorted list, space-separated
print(' '.join(map(str, numbers)))