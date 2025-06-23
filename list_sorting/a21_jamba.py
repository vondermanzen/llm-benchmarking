import sys

input_list = [int(x) for x in sys.stdin.readline().split()]
input_list.sort()
print(' '.join(map(str, input_list)))