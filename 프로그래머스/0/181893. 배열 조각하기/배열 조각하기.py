def solution(arr, query):
    for idx, val in enumerate(query):
        if idx % 2 == 1: # 홀수 인덱스
            arr = arr[val : ]
        else: # 짝수 인덱스
            arr = arr[ : val + 1]
    
    return arr