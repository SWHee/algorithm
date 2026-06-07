def solution(numlist, n):
    # n 기준 가까운 수부터 정렬
    
    numlist.sort(key=lambda x : (abs(x - n), -x))

    return numlist