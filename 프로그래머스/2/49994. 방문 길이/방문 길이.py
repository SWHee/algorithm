def solution(dirs):
    # 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이
    # dirs는 string
    commands = list(dirs)
    
    visited = set()
    cur_x, cur_y = 0, 0
    
    # 갔던 길을 또 지나간 경우
    # (-5, -5) 좌표를 넘어간 경우 -> 5개 이상 나올경우
    for command in commands:
        prev_x, prev_y = cur_x, cur_y
        next_x, next_y = cur_x, cur_y
        
        if command == 'U':
            next_y += 1
        elif command == 'D':
            next_y -= 1
        elif command == 'R':
            next_x += 1
        elif command == 'L':
            next_x -= 1
        
        # 경계선 체크
        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            continue
        
        cur_x, cur_y = next_x, next_y
        
        path1 = ((prev_x, prev_y), (cur_x, cur_y))
        path2 = ((cur_x, cur_y), (prev_x, prev_y))
        
        visited.add(path1)
        visited.add(path2)

    return len(visited) // 2