import sys

def main():
    input_line = sys.stdin.readline().strip()
    
    integer_list = [int(x) for x in input_line.split()]
    
    sorted_list = sorted(integer_list)
    
    print(' '.join(map(str, sorted_list)))

if __name__ == '__main__':
    main()