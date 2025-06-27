# Read input from standard input
input_line = input().strip()

# Split the input into a list of strings and convert to integers
numbers = list(map(int, input_line.split()))

# Sort the list in ascending order
numbers.sort()

# Convert back to strings and join with spaces
output = ' '.join(map(str, numbers))

# Print the sorted list
print(output)

