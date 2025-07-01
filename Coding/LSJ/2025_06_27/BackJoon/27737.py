import sys
input = sys.stdin.readline

sentence = input().strip()
n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())