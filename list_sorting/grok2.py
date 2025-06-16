import sys

# Read input from standard input
input_line = sys.stdin.readline().strip()

# Convert input string to list of integers
numbers = [int(num) for num in input_line.split()]

# Sort the list of integers in ascending order
sorted_numbers = sorted(numbers)

# Convert sorted list back to space-separated string
output_line = ' '.join(map(str, sorted_numbers))

# Print the sorted list to standard output
print(output_line)