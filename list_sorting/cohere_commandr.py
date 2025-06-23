import sys

# Reading input as a string
user_input = sys.stdin.readline().strip()

# Converting string to a list of integers
int_list = list(map(int, user_input.split()))

# Sorting the list of integers
int_list.sort()

# Printing the sorted list
print(' '.join(map(str, int_list)))