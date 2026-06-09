def solution(order):
    # 아메리카노 = 4500
    # 카페라떼 = 5000
    
    # "anything" = 차가운 아메리카노
    
    answer = 0
    
    for menu in order:
        if "cafelatte" in menu:
            answer += 5000
        else:
            answer += 4500
            
    return answer