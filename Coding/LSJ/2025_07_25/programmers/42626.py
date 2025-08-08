import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1 and scoville[0] < K:
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir + sec*2)
        answer += 1
    
    return answer if scoville[0] >= K else -1