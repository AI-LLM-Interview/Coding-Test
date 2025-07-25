def solution(n, results):
    answer = 0
    
    win=[[] for _ in range(n + 1)]
    lose=[[] for _ in range(n + 1)]
    
    for result in results:
        winner = result[0]
        loser = result[1]
        win[winner].append(loser)
        lose[loser].append(winner)
        
#     print(win)
#     print()
#     print(lose)

    def dfs(graph, start, visited):
        for j in graph[start]:
            if not visited[j]:
                visited[j] = True
                dfs(graph, j, visited)
                
    # 각 선수별로 전체 승패 관계 탐색
    for i in range(1, n + 1):
        win_visited = [False] * (n + 1)
        lose_visited = [False] * (n + 1)

        win_visited[i] = True
        lose_visited[i] = True

        dfs(win, i, win_visited)   # i가 이긴 사람들 모두 찾기
        dfs(lose, i, lose_visited) # i가 진 사람들 모두 찾기

        total = sum(win_visited) + sum(lose_visited) - 2  # 자기 자신 2번 제외

        if total == n - 1:
            answer += 1

    return answer