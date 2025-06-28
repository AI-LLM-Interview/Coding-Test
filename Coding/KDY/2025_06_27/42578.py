from collections import Counter

def solution(clothes):
    answer = 1
    name = []
    category = []
    
    for x in clothes:
        name.append(x[0])
        category.append(x[1])
        
    count = Counter(category)
    print(count)
    for c in count:
        answer *= count[c]+1
    answer = answer -1
    return answer