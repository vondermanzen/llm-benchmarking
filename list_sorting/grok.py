import sys

# Read input from standard input
input_line = sys.stdin.readline().strip()
# Convert input string to list of integers
numbers = [int(x) for x in input_line.split()]
# Sort the list in ascending order
numbers.sort()
# Print the sorted list, space-separated
print(' '.join(map(str, numbers)))