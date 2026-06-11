def solution(l, r):
    # 없는 경우 -1 리턴 예외처리
    
    answer = []
    
    for cur in range(l, r + 1):
        # 0이나 5 이외의 숫자가 들었다면 
        if all(char in "05" for char in str(cur)):
            answer.append(cur)
            
    if len(answer) == 0:
        answer.append(-1)
        
    return answer