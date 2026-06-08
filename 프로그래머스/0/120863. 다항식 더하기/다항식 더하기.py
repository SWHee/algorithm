def solution(polynomial):
    # 항과 연산기호 사이에는 항상 공백이 존재
    # 시작이나 끝에는 공백이 없음
    # 계수 1은 생략
    x_sum, num_sum = 0, 0
    terms = polynomial.split(" + ")
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term.replace('x', ''))
        else:
            num_sum += int(term)
        
    answer = []
    
    if x_sum > 0:
        if x_sum == 1:
            answer.append("x")
        else:
            answer.append(f"{x_sum}x")

    if num_sum > 0:
        answer.append(str(num_sum))
        
    return " + ".join(answer)