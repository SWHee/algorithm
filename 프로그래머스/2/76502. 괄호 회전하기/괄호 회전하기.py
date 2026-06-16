def solution(s):
    # 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s
    # 왼쪽으로 x칸 만큼 회전시켜야 올바른 괄호 문자열이 되게 하고, x 출력
    # 0 ~ len(s) 까지 수행. 맞으면 카운트 +1 누적
    x = 0
    pair = {']': '[', '}': '{', ')': '('}
    
    
    for i in range(len(s)):
        shifted = s[i:] + s[:i]
        
        
        stack = []
        is_valid = True
        
        
        for char in shifted:
            if char in ['[', '{', '(']:
                stack.append(char)
            else:
                if not stack or stack[-1] != pair[char]:
                    is_valid = False
                    break
                else:
                    stack.pop() 
        
        
        if is_valid and not stack:
            x += 1
    
    return x