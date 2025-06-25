import sys

numbers = list(map(int, sys.stdin.read().strip().split()))
print(' '.join(map(str, sorted(numbers))))
