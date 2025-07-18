import heapq
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(board):
    n = len(board)
    
    cost = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    # 비용, y, x, 방향
    pq = []
    
    # 시작점에서 우, 하 방향으로 시작 가능
    if n > 1: 
        
        # 오른쪽으로 갈 수 있으면
        if board[0][1] == 0:
            cost[0][1][3] = 100
            heapq.heappush(pq, (100, 0, 1, 3))
        
        # 아래쪽으로 갈 수 있으면
        if board[1][0] == 0:
            cost[1][0][1] = 100 
            heapq.heappush(pq, (100, 1, 0, 1))
    
    while pq:
        current_cost, y, x, direction = heapq.heappop(pq)
        
        # 이미 더 적은 비용으로 방문했다면 스킵
        if current_cost > cost[y][x][direction]:
            continue
        
        # 4방향으로 이동 시도
        for next_dir, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = current_cost + 100
                
                # 방향이 바뀌면 코너 비용 추가
                if direction != next_dir:
                    new_cost += 500
                
                # 더 적은 비용일 때
                if new_cost < cost[ny][nx][next_dir]:
                    cost[ny][nx][next_dir] = new_cost
                    heapq.heappush(pq, (new_cost, ny, nx, next_dir))
    
    return min(cost[n-1][n-1])