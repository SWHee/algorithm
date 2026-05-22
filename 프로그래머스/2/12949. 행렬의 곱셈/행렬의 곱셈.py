def solution(arr1, arr2):
    
    # A * B 행렬 곱셈을 하면 결과 행렬의 크기는
    # [arr1의 세로 길이 * arr2의 가로 길이]
    
    # arr1[i][k] * arr2[k][j]
    
    row1, col1 = len(arr1), len(arr1[0])
    row2, col2 = len(arr2), len(arr2[0])
    
    answer = [[0] * col2 for i in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    
    return answer