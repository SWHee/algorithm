def solution(score):
    avg_list = []
    
    # 각 학생의 평균 점수를 구해서 리스트에 저장
    for s in score:
        eng = s[0]
        math = s[1]
        avg = (eng + math) / 2
        avg_list.append(avg)
        
    # 등수를 매기기 위해 내림차순 정렬된 새 리스트 생성
    sorted_avg = sorted(avg_list, reverse=True)
    
    answer = []
    # 원본 평균 리스트를 돌며 등수 매기기
    for avg in avg_list:
        rank = sorted_avg.index(avg) + 1
        answer.append(rank)
        
    return answer