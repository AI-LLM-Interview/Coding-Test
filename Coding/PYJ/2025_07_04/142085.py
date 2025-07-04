import heapq

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        # 병사로 막고 최대 힙에 넣기 (음수로 저장)
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        
        # 병사가 부족하면 가장 많이 소모된 라운드를 무적권으로 되돌리기
        if n < 0:
            if k == 0:
                return i  # 이 라운드에서 막을 수 없음
            max_enemy = -heapq.heappop(heap)
            n += max_enemy  # 무적권으로 바꿔서 병사 회수
            k -= 1
    
    return len(enemy)
