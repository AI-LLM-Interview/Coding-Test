def solution(name):
    answer = 0
    
    # 1. 알파벳 변경(▲▼) 횟수 계산
    for char in name:
        updown = ord(char) - ord('A')
        answer += min(updown, 26 - updown) #양쪽으로 이동가능하니까 
    
    # 2. 커서 이동(◀▶) 최솟값 계산
    move = len(name) - 1  # 기본 오른쪽으로만 이동하는 경우

    for i in range(len(name)):
        next_idx = i + 1
        # 연속된 A가 있는 구간을 찾음
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        
        # 오른쪽으로 갔다가 왼쪽으로 되돌아오는 경우 or 반대로 먼저 끝쪽 갔다가 돌아오는 경우
        distance = min(i * 2 + len(name) - next_idx,     # 오른쪽 → 왼쪽
                       (len(name) - next_idx) * 2 + i)   # 왼쪽 → 오른쪽
        move = min(move, distance)

    return answer + move