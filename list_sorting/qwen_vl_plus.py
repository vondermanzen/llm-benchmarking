# Read the list of integers as a string with spaces separated values
input_list = input().split()
# Convert each element into an integer using map function and then convert it back to a list after sorting
sorted_list = ' '.join(map(str, sorted(list(map(int, input_list)))))
print(sorted_list)