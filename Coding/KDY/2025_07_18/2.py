from collections import deque

def solution(board):
    answer = 10000000000
    n = len(board)
    
    
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]

    cost = [[[10000000] * 4 for _ in range(n)] for _ in range(n)]

    q = deque()

    # 처음 시작점에서 오른쪽, 아래방향만 출발 가능
    for d in [1, 3]:
        cost[0][0][d] = 0
        q.append((0, 0, d, 0))  # x, y, 방향, 누적비용

    while q:
        x, y, direction, c = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                # 같은 방향이면 직선: +100, 아니면 코너: +600
                if direction == i:
                    nc = c + 100
                else:
                    nc = c + 600

                if cost[nx][ny][i] > nc:
                    cost[nx][ny][i] = nc
                    q.append((nx, ny, i, nc))

    for d in range(4):
        answer = min(answer, cost[n-1][n-1][d])

    return answer
