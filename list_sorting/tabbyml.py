def sort_list(input_list):
    input_list.sort()
    return input_list

# Read input from stdin
input_list = list(map(int, input().split()))

# Sort the list
sorted_list = sort_list(input_list)

# Print sorted list to stdout
print(' '.join(map(str, sorted_list)))