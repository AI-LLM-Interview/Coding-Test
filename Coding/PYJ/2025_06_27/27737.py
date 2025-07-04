import sys, math
from collections import deque

input = sys.stdin.readline


# 한 덩어리의 크기를 구하는 함수
def bfs(x, y):
    queue = deque([(x, y)])
    # 방문 처리
    boards[x][y] = 1
    # 연결된 영역 변수 정의
    areas = 1

    while queue:
        x, y = queue.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]
            # 영역 내 버섯 자랄 수 있는 칸 있는지 확인
            if 0 <= nx < N and 0 <= ny < N and boards[nx][ny] == 0:
                # 방문 처리
                boards[nx][ny] = 1
                queue.append((nx, ny))
                # 영역 개수 카운트
                areas += 1
                # 최소 하나로
    return areas

# N, M, K = 판의 크기, 전체 포자 개수, 한 번에 자랄 수 있는 버섯 개수
N, M, K = map(int, input().split())

# 나무판 상태 입력
boards = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 이동 방향 정의
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 전체 필요 포자 개수 변수 정의
total_nums = 0

# 최소 하나의 포자 사용했는지 여부 나타내는 변수 정의
use_seed = False

# 전체 탐색해 버섯 자랄 수 있는 칸 찾기
for i in range(N):
    for j in range(N):
        if boards[i][j] == 0:
            # BFS 수행
            areas = bfs(i, j)
            # 남은 포자 개수 얻기
            nums = math.ceil(areas / K)
            # 누적합 계산
            total_nums += nums
            # 포자 사용함 기록
            use_seed = True

# 결과 출력
if not use_seed:
    print('IMPOSSIBLE')
elif total_nums <= M:
    print('POSSIBLE')
    print(M - total_nums)
else:
    print('IMPOSSIBLE')


#| 항목    | BFS (너비 우선)     | DFS (깊이 우선)          |
#| ----- | --------------- | -------------------- |
#| 탐색 방식 | 가까운 칸부터 → 퍼지듯이  | 한 방향으로 쭉 → 끝까지       |
#| 사용 구조 | `queue` (deque) | **`stack` or 재귀함수**  |
#| 순서    | 층별로 확장          | 길게 파고들기              |
#| 대표 구조 | `while queue:`  | `def dfs():` + 재귀 호출 |


# import sys
# import math
# sys.setrecursionlimit(1000000)  # 재귀 깊이 제한 해제

# input = sys.stdin.readline

# N, M, K = map(int, input().split())
# boards = [list(map(int, input().split())) for _ in range(N)]

# # 상하좌우 방향
# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# def dfs(x, y):
#     # 방문 처리
#     boards[x][y] = 1
#     size = 1

#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < N and 0 <= ny < N and boards[nx][ny] == 0:
#             size += dfs(nx, ny)  # 연결된 곳 계속 탐색
#     return size

# total_spores = 0
# use_seed = False

# for i in range(N):
#     for j in range(N):
#         if boards[i][j] == 0:
#             area = dfs(i, j)
#             spores_needed = math.ceil(area / K)
#             total_spores += spores_needed
#             use_seed = True

# if not use_seed:
#     print("IMPOSSIBLE")
# elif total_spores <= M:
#     print("POSSIBLE")
#     print(M - total_spores)
# else:
#     print("IMPOSSIBLE")
