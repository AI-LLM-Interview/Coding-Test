def solution(name):
    
    # 1. 각 문자를 만드는데 필요한 최소 조작 횟수 계산
    def cost(char):
        ascii = ord(char) - ord('A')
        return min(ascii, 26 - ascii)
        
    # 각 문자 변경 비용 계산
    char_costs = [cost(char) for char in name]
    total_char_cost = sum(char_costs)
    
    # 2. 커서 이동 최적화
    n = len(name)
    if n == 1:
        return total_char_cost
    
    # 기본적으로 순서대로 이동하는 경우 (오른쪽으로만)
    min_move = n - 1
    
    # 각 위치에서 되돌아가는 경우를 고려
    for i in range(n):
        next_pos = i + 1
        while next_pos < n and name[next_pos] == 'A':
            next_pos += 1
        
        # 앞쪽을 처리하고 뒤로 돌아가서 뒤쪽 처리
        forward_back = i + i + (n - next_pos)
        
        # 뒤쪽을 먼저 처리하고 앞쪽 처리
        back_forward = (n - next_pos) + (n - next_pos) + i
        
        # 최소값 업데이트
        min_move = min(min_move, forward_back, back_forward)
    
    return total_char_cost + min_move