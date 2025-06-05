import sys

def main():
    # Read input from stdin
    input_line = sys.stdin.readline()
    
    # Split the input line into individual strings and convert to integers
    numbers = list(map(int, input_line.strip().split()))
    
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Convert the sorted numbers back to strings and join them with spaces
    output = ' '.join(map(str, sorted_numbers))
    
    # Print the result
    print(output)

if __name__ == "__main__":
    main()