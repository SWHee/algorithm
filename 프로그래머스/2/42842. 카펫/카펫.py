def solution(brown, yellow):
    '''
    노란색 격자 -> 가로 길이 >= 세로 길이 
    row = 가로, col = 세로
    
    answer[0] = 카펫의 가로 길이
    answer[1] = 카펫의 세로 길이
    '''
    answer = []
    total = brown + yellow
    
    for col in range(1, total + 1):
        if total % col == 0:
            row = total // col
            if row >= col:
                if (row - 2) * (col - 2) == yellow:
                    answer = [row, col]
                    break   # 조기에 찾으면 중단
    
    return answer
