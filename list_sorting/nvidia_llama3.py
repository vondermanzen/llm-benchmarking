import sys

def main():
    # Read input from standard input
    user_input = sys.stdin.readline().strip()
    
    # Split input into a list of integers
    numbers = [int(x) for x in user_input.split()]
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Print the sorted list to standard output, space-separated
    print(' '.join(map(str, sorted_numbers)))

if __name__ == "__main__":
    main()