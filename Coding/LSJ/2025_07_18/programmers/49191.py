def solution(n, results):
    count = [0] * (n + 1)  # 각 선수가 몇 번 언급되는지
    
    for winner, loser in results:
        count[winner] += 1
        count[loser] += 1
    
    answer = 0
    for i in range(1, n + 1):
        if count[i] == n - 1:
            answer += 1
    
    return answer