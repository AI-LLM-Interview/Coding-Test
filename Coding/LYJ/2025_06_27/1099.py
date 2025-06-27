import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
s = input().strip()

word_set = set(words)
length = len(s)
INF = 10**9
dp = [INF] * (length + 1)
dp[0] = 0

for i in range(1, length + 1):
    for j in range(i):
        if s[j:i] in word_set:
            dp[i] = min(dp[i], dp[j] + 1)

print(0 if dp[length] == INF else dp[length])
