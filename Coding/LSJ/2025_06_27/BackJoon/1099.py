dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)