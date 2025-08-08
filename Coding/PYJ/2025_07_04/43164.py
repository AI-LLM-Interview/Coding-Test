def solution(tickets):
    from collections import defaultdict

    # 그래프 만들기
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)

    # 역알파벳 순으로 정렬
    for key in graph:
        graph[key].sort(reverse=True)  

    path = []

    def dfs(curr):
        # 현재 공항에서 갈 수 있는 모든 티켓 사용
        while graph[curr]:
            next = graph[curr].pop() # 뒤에서 부터 하나씩 꺼냄(a -> z)
            dfs(next)
        path.append(curr)  # 더 이상 갈 곳 없으면 경로에 추가

    dfs("ICN")
    return path[::-1]  
