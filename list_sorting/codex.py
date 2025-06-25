# Read input from standard input
input_line = input().strip()

# Convert input string to list of integers
numbers = list(map(int, input_line.split()))

# Sort the list in ascending order
numbers.sort()

# Print the sorted list as space-separated integers
print(' '.join(map(str, numbers)))
