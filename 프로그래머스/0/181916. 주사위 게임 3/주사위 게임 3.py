def solution(a, b, c, d):
    # 주사위 4개
    # 4개 모두 p -> += 1111*p
    # 3개만 같다 -> (10 × p + q)^2 
    # 2개만 같다 -> 나머지 2개 서로 같다 -> (p + q) × |p - q|
    #          -> 나머지 2개 서로 다르다 -> q × r (나머지 2개 곱)
    # 모두 다르다 -> 가장 작은 숫자만큼 얻기
    
    dice_count = {
        "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0
    }
    
    # 딕셔너리 값 추가를 위해 리스트로 변환 후 카운팅
    nums = [a, b, c, d]
    for num in nums:
        dice_count[str(num)] += 1
    
    # 카운팅 된 것만 리스트로 뽑아내기
    have_count = []
    for key, value in dice_count.items():
        if value > 0:
            have_count.append((int(key), value))
                  
    # 가장 큰 횟수로 정렬                              
    have_count.sort(key=lambda x: x[1], reverse=True)
    
    # [조건 1] 4개 모두 같은 숫자인 경우 (리스트의 맨 앞 횟수가 4)
    if have_count[0][1] == 4:
        p = have_count[0][0]
        return 1111 * p
        
    # [조건 2] 3개만 같은 숫자인 경우 (리스트의 맨 앞 횟수가 3)
    elif have_count[0][1] == 3:
        p = have_count[0][0] # 3번 나온 수
        q = have_count[1][0] # 1번 나온 수
        return (10 * p + q) ** 2
        
    # [조건 3 & 4] 가장 많이 나온 횟수가 2개인 경우 (2가지로 나뉨)
    elif have_count[0][1] == 2:
        # 나머지 2개도 서로 같은 경우
        if len(have_count) == 2:
            p = have_count[0][0]
            q = have_count[1][0]
            return (p + q) * abs(p - q)
        # 나머지 2개는 서로 다른 경우 (예: 2개, 1개, 1개 총 3종류의 숫자일 때)
        else:
            q = have_count[1][0]
            r = have_count[2][0]
            return q * r
            
    # [조건 5] 모두 다른 숫자인 경우 (모두 1개씩만 나와서 정렬해도 맨 앞이 1일 때)
    else:
        # 모두 다를 때는 가장 작은 숫자를 찾아야 하므로 
        # 기존 주사위 입력값인 nums에서 min() 함수로 최소값을 구합니다.
        return min(nums)