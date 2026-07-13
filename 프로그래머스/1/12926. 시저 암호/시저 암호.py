def solution(s, n):
    # 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
    # 문자열 s와 거리 n
    
    answer = []

    for char in s:
        if char.isupper():
            answer.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        elif char.islower():
            answer.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        else:
            answer.append(char)

    # 문자열 반환을 위해서
    return ''.join(answer)