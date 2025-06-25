#!/usr/bin/env python3

def main():
    # Read space-separated integers from standard input
    input_line = input().strip()
    
    # Parse the input into a list of integers
    numbers = list(map(int, input_line.split()))
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Print the sorted list as space-separated integers
    print(' '.join(map(str, sorted_numbers)))

if __name__ == '__main__':
    main()
