def solution(t, p):
    target_length = len(p)
    # p 문자열을 int로 변환
    target = int(p)
    count = 0

    for start in range(len(t) - target_length + 1):
        number = int(t[start:start + target_length])

        if number <= target:
            count += 1

    return count