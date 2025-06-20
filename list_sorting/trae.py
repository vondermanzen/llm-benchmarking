def main():
    try:
        # Read space-separated integers from input
        numbers = list(map(int, input().strip().split()))
        
        # Sort the numbers in ascending order
        sorted_numbers = sorted(numbers)
        
        # Print the sorted numbers as space-separated values
        print(' '.join(map(str, sorted_numbers)))
        
    except ValueError:
        print("Please enter valid integers separated by spaces")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
