def main():
    # Read space-separated integers from standard input
    input_line = input().strip()
    
    # Convert the input string to a list of integers
    numbers = list(map(int, input_line.split()))
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Convert the sorted list back to a space-separated string and print it
    output_line = ' '.join(map(str, numbers))
    print(output_line)

if __name__ == "__main__":
    main()
