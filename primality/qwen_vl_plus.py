import math
from random import randint

def miller_rabin(n):
    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for _ in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return False
    
    if n <= 3:
        return [True] + ['False', 'Neither'][n < 2]
    
    # Write n as p*q such that q is odd.
    t = int(math.log2(n))
    while ((q := n // 2 ** t)) % 2 == 0:
        t -= 1
        
    r = t; b = n - 1
    while b & 1 == 0:
        b >>= 1
    
    for i in range(4): 
        a = randint(2, min(b.bit_length(), n - 2))
        if not check(a, r, b, n):
            return 'Composite'
            
    return 'Prime'

T = int(input())
for _ in range(T):
    num_str = input()
    try:
        num_int = int(num_str)
        print(miller_rabin(num_int))
    except ValueError:
        pass