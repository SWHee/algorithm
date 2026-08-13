def solution(n):
    '''
    64  32  16  8   4   2   1
    1   0   0   1   1   1   0
    
    1. n값 1까지 나누기 -> 1의 개수 카운트
    2. n값 기준 1씩 늘려가며
        1) 1까지 while문 나눗셈 -> 나머지가 1이 생길때마다 +
        2) 마지막에 1의 개수 카운트. 같으면 해당 i 값 리턴
    '''
    next_num = n + 1
    
    cur_count = 0
    next_count = 0
    
    while n >= 1:
        if n % 2 == 1:
            cur_count += 1
        n //= 2

    while True:
        next_count = 0
        n = next_num

        while n >= 1:
            if n % 2 == 1:
                next_count += 1
            n //= 2

        if next_count == cur_count:
            return next_num

        next_num += 1