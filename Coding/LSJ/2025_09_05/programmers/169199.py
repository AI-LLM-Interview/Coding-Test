from collections import deque

def solution(board):
    rows = len(board)
    cols = len(board[0])
    
    # 로봇 시작 위치와 목표 위치 찾기
    start_row = start_col = goal_row = goal_col = -1
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                start_row, start_col = i, j
            elif board[i][j] == 'G':
                goal_row, goal_col = i, j
    
    # 방향 벡터: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐와 방문 체크 집합
    queue = deque([(start_row, start_col, 0)])  # (row, col, moves)
    visited = set()
    visited.add((start_row, start_col))
    
    def slide(row, col, direction):
        """한 방향으로 미끄러져 이동하는 함수"""
        dr, dc = directions[direction]
        new_row, new_col = row, col
        
        # 장애물이나 경계에 부딪힐 때까지 이동
        while True:
            next_row = new_row + dr
            next_col = new_col + dc
            
            # 경계를 벗어나거나 장애물에 부딪히면 멈춤
            if (next_row < 0 or next_row >= rows or 
                next_col < 0 or next_col >= cols or 
                board[next_row][next_col] == 'D'):
                break
            
            new_row, new_col = next_row, next_col
        
        return new_row, new_col
    
    # BFS 탐색
    while queue:
        current_row, current_col, moves = queue.popleft()
        
        # 목표에 도달했는지 확인
        if current_row == goal_row and current_col == goal_col:
            return moves
        
        # 4방향으로 이동 시도
        for direction in range(4):
            new_row, new_col = slide(current_row, current_col, direction)
            
            # 이동하지 않았다면 (같은 위치라면) 건너뛰기
            if new_row == current_row and new_col == current_col:
                continue
            
            # 이미 방문한 위치라면 건너뛰기
            if (new_row, new_col) in visited:
                continue
            
            # 방문 표시하고 큐에 추가
            visited.add((new_row, new_col))
            queue.append((new_row, new_col, moves + 1))
    
    # 목표에 도달할 수 없는 경우
    return -1