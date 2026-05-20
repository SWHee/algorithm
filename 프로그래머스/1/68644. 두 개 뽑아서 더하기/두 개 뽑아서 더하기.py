def solution(numbers):
    # 서로 다른 인덱스(2 이상 100 이하)
    # 더해서 만들 수 있는 모든 수를 배열에 담기
    # 배열에 오름차순으로 담아서 리턴
    
    # n개의 요소 -> 구할 수 있는 모든 수의 개수 = n-1 + n-2 + ... + 1
    
    combination = []
    
    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            combination.append(numbers[x] + numbers[y])
    
    answer = list(set(combination))
    answer.sort()
    return answer