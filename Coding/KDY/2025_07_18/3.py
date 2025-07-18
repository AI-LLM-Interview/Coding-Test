def dfs(i, computers, visited):
    visited[i] = True
    for j in range(len(computers[i])):
        if computers[i][j] == 1 and not visited[j]:
            dfs(j, computers, visited)

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i, computers,visited)
            answer += 1
    return answer