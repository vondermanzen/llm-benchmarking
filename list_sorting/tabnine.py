# Read input from standard input
input_str = input()

# Split the input string into a list of integers
input_list = list(map(int, input_str.split()))

# Sort the list in ascending order
sorted_list = sorted(input_list)

# Print the sorted list to standard output
print(' '.join(map(str, sorted_list)))