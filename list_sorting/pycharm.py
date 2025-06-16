def main():
    # Read a single line of input containing space-separated integers
    input_line = input().strip()

    # Convert the input string to a list of integers
    numbers = list(map(int, input_line.split()))

    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)

    # Convert the sorted integers back to space-separated string and print
    result = ' '.join(map(str, sorted_numbers))
    print(result)

if __name__ == "__main__":
    main()
