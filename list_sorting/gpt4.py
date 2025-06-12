numbers = list(map(int, input().strip().split()))
numbers.sort()
print(' '.join(map(str, numbers)))