import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rooms = []
for i in range(n):
    room = list(map(int, input().split()))
    for j in room:
        rooms.append((j, i)) 
    
rooms.sort()

min_ans = 1000000000
left = 0
classes = [0] * n
now = 0

for i in range(len(rooms)):
    num, cnt = rooms[i]
    
    if classes[cnt] == 0:
        now += 1
    classes[cnt] += 1
    
    while now == n:
        diff = rooms[i][0] - rooms[left][0]
        min_ans = min(min_ans, diff)
        
        left_num, left_cnt = rooms[left]
        classes[left_cnt] -= 1
        if classes[left_cnt] == 0:
            now -= 1
        left += 1
print(min_ans)