def solution(n):
    '''
    n에 대한 표현 가능 방법의 수 리턴
    단, 연속한 자연수만 가능.
    
    1. i부터 n까지 하나씩
        1) sum이 n을 넘지 않을 때까지 더한다
        2) sum이 n이랑 같은 경우에만 answer += 1
    '''
    answer = 0
    
    for i in range(1, n + 1):
        total = 0
        current = i
        
        while total < n:
            total += current
            current += 1
            
        if total == n:
            answer += 1
            
    return answer
