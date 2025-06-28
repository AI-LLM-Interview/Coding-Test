from collections import deque

n, m, k = map(int, input().split()) # 포자 개수 M, 포자 확산 범위 K
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
total_need = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def func(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt