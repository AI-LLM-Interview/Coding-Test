import heapq

N, M = map(int, input().split())
arr = [sorted(map(int, input().split())) for _ in range(N)]
heap = []
maxV = 0
for i in range(N):
    v = arr[i][0]
    heapq.heappush(heap, (v, i, 0))
    maxV = max(maxV, v)

ans = float('inf')
while heap:
    v, cls, idx = heapq.heappop(heap)
    ans = min(ans, maxV - v)
    if idx + 1 == M:
        break
    nxt = arr[cls][idx + 1]
    heapq.heappush(heap, (nxt, cls, idx + 1))
    maxV = max(maxV, nxt)

print(ans)
