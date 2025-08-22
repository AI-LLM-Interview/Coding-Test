import heapq

def solution(n, works):
    # 모든 작업 완료
    if n >= sum(works):
        return 0
    
    # 최대 힙을 위해 음수로 변환
    heap = [-work for work in works]
    heapq.heapify(heap)
    
    # n시간 동안 가장 큰 작업량부터 1씩 줄임
    for _ in range(n):
        max_work = -heapq.heappop(heap)
        if max_work > 0:
            heapq.heappush(heap, -(max_work - 1))
        else:
            heapq.heappush(heap, 0)
    
    # 야근 피로도 계산 (제곱의 합)
    return sum(work * work for work in [-w for w in heap])