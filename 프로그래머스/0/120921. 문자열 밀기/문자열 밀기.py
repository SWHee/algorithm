def solution(A, B):
    # B를 두 번 더한 문자열에서 A의 시작 위치를 찾음
    return (B + B).find(A)