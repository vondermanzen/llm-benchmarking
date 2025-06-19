input_str = input()
numbers = [int(x) for x in input_str.split()]
numbers.sort()
print(*numbers)