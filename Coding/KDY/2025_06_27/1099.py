from collections import Counter

sentence = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]
INF = float('inf')
dp = [INF] * (len(sentence) + 1)
dp[0] = 0

for i in range(len(sentence)):
    if dp[i] == INF:
        continue
    for word in words:
        if i + len(word) > len(sentence):
            continue
        part = sentence[i:i+len(word)]
        if Counter(part) != Counter(word):
            continue
        
        # 비용 계산
        cost = sum(1 for a, b in zip(part, word) if a != b)
        dp[i+len(word)] = min(dp[i+len(word)], dp[i] + cost)