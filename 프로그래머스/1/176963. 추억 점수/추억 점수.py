def solution(name, yearning, photo):
    # 그리워하는 사람의 이름을 담은 문자열 배열 name
    # 각 사람별 그리움 점수를 담은 정수 배열 yearning
    # 인물의 이름을 담은 이차원 문자열 배열 photo
    
    answer = [] # 이차원 배열에서 일치하는 사람만 더해서 리스트에 append
    
    # 딕셔너리로 바꿔야겠는데 ? 해당하는 키와 값으로 초기화하고, 키 있으면 그 점수 tmp로 더하기로
    
    score = dict(zip(name, yearning))
    
    for row in photo:
        tmp = 0
        
        for n in row:
            if n in score:
                tmp += score.get(n)
                
        answer.append(tmp)
        
    return answer