import heapq

def solution(n, k, enemy):
    dead = []

    for i in range(len(enemy)):
        x = enemy[i]    # 지금 처치할 적
        heapq.heappush(dead, -x)    # 힙에 적을 추가 [-4, -2]
        n -= x      # 처치했다고 계산

        if n < 0:       # 처치하지 못할때
            if k == 0:      # 무적권도 없으면, 종료
                return i
            
            # 무적권 있을 때,
            n += -heapq.heappop(dead)   # 처치한 적 되돌리기
            k -= 1      # 무적권 사용

    return len(enemy)   # 끝까지 다 막으면 전체 길이 출력


########### 오답 기록

#     answer = 0
#     dead = []   
#     for i in range(len(enemy)):   
#         # 1.병사가 충분하면 사용
#         if n >= enemy[i]:
#             n -= enemy[i]
#             heapq.heappush(dead, -enemy[i])
#             answer += 1
#             # print(1,'|',k,n,dead)  
#         # 2.병사가 부족할때
#         elif n < enemy[i]:
#             # 2-1 무적권이 있으면(+빈배열이 아니면)
#             if k>0 and dead:
#                 # 값 비교
#                 x = -heapq.heappop(dead)
#                 if x >= enemy[i]:
#                     # 무적권 사용한 후
#                     k -= 1
#                     n += x
#                     # 병사 사용
#                     if n >= enemy[i]:
#                         n -= enemy[i]
#                         heapq.heappush(dead, -enemy[i])
#                         answer += 1
#                         # print('2-1','|',k,n,dead)
#                     else:
#                         return answer             
#                 else:
#                     k -= 1
#                     heapq.heappush(dead, -enemy[i])
#                     heapq.heappush(dead, x)
#                     answer += 1
#             # 2-2 무적권 있는데 힙이 비어있으면
#             elif k>0 and (not dead):
#                 k -= 1
#                 answer += 1
#                 # print('2-2','|',k,n,dead)
#             # 2-3 무적권이 없으면 결과 리턴
#             elif k <= 0:
#                 # print('2-3','|',k,n,dead)
#                 return answer
#     return answer