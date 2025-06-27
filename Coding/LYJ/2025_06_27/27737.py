from collections import deque
import math

# 입력
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    size = 1

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and grid[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    size += 1
    return size

total_spores = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            area_size = bfs(i, j)
            spores_needed = math.ceil(area_size / K)
            total_spores += spores_needed

if total_spores == 0 or total_spores > M:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(M - total_spores)
