import heapq

n, m = map(int, input().split())
array = []
answer = int(1e9) # 차이가 최소
queue = [] # heapq 는 가장 작은 요소를 뱉어냄
max_value = 0 # ex) 14
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    array.append(data)
    max_value = max(max_value, data[0])
    heapq.heappush(queue, (data[0],i)) # data 중에 가장 작은 값 ex) 12, 7, 14를 넣기 위함
pointer = [0] * (n+1) # n 개 클래스가 지금 가리키는 각각의 인덱스

while queue:
    x = heapq.heappop(queue) # ex) 7
    min_value = x[0]
    index = x[1] # 속한 그룹
    answer = min(max_value - min_value, answer) # 14-7 = 7
    if pointer[index] == m-1:
        break # array에서 값 꺼낼 때 index 초과 문제 방지
    pointer[index] += 1
    heapq.heappush(queue, (array[index][pointer[index]],index))
    max_value = max(max_value, array[index][pointer[index]])

print(answer)