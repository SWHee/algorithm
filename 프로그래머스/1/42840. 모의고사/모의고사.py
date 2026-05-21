def solution(answers):
    # 정답이 들어있는 배열 answers
    
    # '모든' 문제를 찍는다
    
    # 1번 -> 1,2,3,4,5 / 5개
    # 2번 -> 2,1,2,3,2,4,2,5 / 8개
    # 3번 -> 3,3,1,1,2,2,4,4,5,5 / 10개
    
    # 가장 많은 문제를 맞힌 사람 배열에 담기
    # 여럿일 경우 오름차순 정렬
    
    # 1번, 2번, 3번 사람 각자 맞은 개수 구해서 리스트에 전부 넣기
    # answer.len 2개 이상이면 정렬하기
    
    answer = []
    
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    counts = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        for i, pat in enumerate(patterns):
            if pat[idx % len(pat)] == ans:
                counts[i] += 1
    
    mostCount = max(counts)
    
    # 혹시 맞은 개수 같은 사람 있으면
    for i, count in enumerate(counts):
        if counts[i] == mostCount:
            answer.append(i + 1)
    
    
    return answer