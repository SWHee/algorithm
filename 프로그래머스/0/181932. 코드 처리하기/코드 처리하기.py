def solution(code):
    # code 문자열
    # 한글자씩 읽으면서 1 만나면 mode 바꾸기
    # 문자열 code를 통해 만들어진 문자열 ret를 return
    mode = 0
    ret = ""
    
    for idx, val in enumerate(code):
        # 1인 경우
        if val == "1":
            if mode == 0:
                mode = 1
            elif mode == 1:
                mode = 0
        
        # 1이 아닌 경우
        else:
            if mode == 0:
                if idx % 2 == 0:
                    ret += val
            elif mode == 1:
                if idx % 2 == 1:
                    ret += val
            
    return ret if ret != "" else "EMPTY"