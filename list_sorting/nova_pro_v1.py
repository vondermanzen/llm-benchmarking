import sys

def main():
    input_data = sys.stdin.read().strip()
    integer_list = list(map(int, input_data.split()))
    sorted_list = sorted(integer_list)
    print(" ".join(map(str, sorted_list)))

if __name__ == "__main__":
    main()