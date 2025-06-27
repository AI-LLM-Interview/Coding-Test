from collections import Counter

def solution(clothes):
    count = Counter([kind for _, kind in clothes])
    answer = 1
    for c in count.values():
        answer *= (c + 1)  
    return answer - 1    
