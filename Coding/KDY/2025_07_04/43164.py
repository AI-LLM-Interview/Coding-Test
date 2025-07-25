from collections import defaultdict
def solution(tickets):
    
    # 티켓 딕셔너리 정의
    graph = defaultdict(list)
    
    for t in tickets:
        start=t[0]
        end=t[1]
        graph[start].append(end)
        graph[start].sort()
    # print(graph)
    
    # 경로 정답
    answer = []
    
    def dfs(now):
        while graph[now]:
            dfs(graph[now].pop(0))
        answer.append(now)

    dfs("ICN")

    return answer[::-1]