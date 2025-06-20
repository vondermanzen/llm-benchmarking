# Read a line of space-separated integers from standard input
input_line = input()

# Split the string into a list of strings
str_numbers = input_line.split()

# Convert the list of strings to a list of integers
numbers = []
for s_num in str_numbers:
    try:
        numbers.append(int(s_num))
    except ValueError:
        # Handle cases where an item might not be a valid integer,
        # though the problem description implies valid integer input.
        # For robustness, we could print an error or skip non-integers.
        # For this problem, we'll assume valid input as per example.
        pass 

# Sort the list of integers in ascending order
numbers.sort()

# Convert the sorted list of integers back to a list of strings
sorted_str_numbers = []
for num in numbers:
    sorted_str_numbers.append(str(num))

# Join the list of strings into a single space-separated string
output_line = " ".join(sorted_str_numbers)

# Print the sorted string to standard output
print(output_line)

# Example Usage (if run directly and not through stdin redirection):
# If the input is: 3 1 4 1 5 9
# The output will be: 1 1 3 4 5 9