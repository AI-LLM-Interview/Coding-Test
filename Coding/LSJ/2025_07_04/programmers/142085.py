import heapq

def solution(n, k, enemy):
    pq = []
    enemy_sum = 0
    for i in range(len(enemy)):
        heapq.heappush(pq, enemy[i])
        if len(pq) > k:
            enemy_sum += heapq.heappop(pq)
        if n < enemy_sum:
            return i
    
    return len(enemy)