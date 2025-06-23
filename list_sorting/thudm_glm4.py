import sys

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
print(' '.join(map(str, numbers)))