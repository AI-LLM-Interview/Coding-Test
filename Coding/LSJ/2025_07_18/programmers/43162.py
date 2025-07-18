def solution(n, computers):
    visited = [0] * n
    answer = 0
    
    def dfs(computer):
        visited[computer] = 1
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                dfs(i)
    
    # 모든 컴퓨터 확인
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer