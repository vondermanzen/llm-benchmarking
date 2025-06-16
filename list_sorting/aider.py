import sys

def main():
    input_line = sys.stdin.read().strip()
    numbers = list(map(int, input_line.split()))
    numbers.sort()
    print(" ".join(map(str, numbers)))

if __name__ == "__main__":
    main()
