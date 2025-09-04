from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 시작점이 막혀있거나 끝점이 막혀있으면 -1 반환
    if maps[0][0] == 0 or maps[n-1][m-1] == 0:
        return -1
    
    # 방향 벡터: 동, 서, 남, 북
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # BFS를 위한 큐와 방문 체크 배열
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        row, col, distance = queue.popleft()
        
        # 목표지점에 도달했는지 확인
        if row == n - 1 and col == m - 1:
            return distance
        
        # 4방향으로 이동 시도
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            
            # 경계 체크
            if 0 <= new_row < n and 0 <= new_col < m:
                # 벽이 아니고 방문하지 않은 곳이라면
                if maps[new_row][new_col] == 1 and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, distance + 1))
    
    # 목표지점에 도달할 수 없는 경우
    return -1