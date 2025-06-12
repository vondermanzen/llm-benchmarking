import sys

input_numbers = list(map(int, sys.stdin.readline().split()))
sorted_numbers = sorted(input_numbers)
print(' '.join(map(str, sorted_numbers)))