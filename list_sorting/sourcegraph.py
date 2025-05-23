# Read space-separated integers from standard input
numbers = list(map(int, input().split()))

# Sort the list in ascending order
numbers.sort()

# Print the sorted numbers as space-separated values
print(' '.join(map(str, numbers)))