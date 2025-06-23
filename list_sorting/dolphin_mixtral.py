import sys

input_list = list(map(int, sys.stdin.read().split()))
input_list.sort()
print(*input_list)