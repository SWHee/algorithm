import math 

def solution(a, b):
    ## 유한소수면 1, 아니면 2
    gcd_num = math.gcd(a, b)
    n = b // gcd_num
    
    while n % 2 == 0:
        n /= 2
        
    while n % 5 == 0:
        n /= 5
    
    return 1 if n ==1 else 2