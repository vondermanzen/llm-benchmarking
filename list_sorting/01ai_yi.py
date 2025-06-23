import sys

# Read input from standard input
input_line = sys.stdin.readline().strip()

# Convert input into a list of integers
numbers = [int(x) for x in input_line.split()]

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Convert the sorted list back into a space-separated string
output = ' '.join(str(x) for x in sorted_numbers)

# Print the sorted list to standard output
print(output)