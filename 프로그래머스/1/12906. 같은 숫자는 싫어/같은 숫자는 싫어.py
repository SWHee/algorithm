from collections import deque

def solution(arr):
    queue = deque(arr)
    answer = []
    
    while queue:
        num = queue.popleft()
        
        if not answer or answer[-1] != num:
            answer.append(num)
            
    return answer
