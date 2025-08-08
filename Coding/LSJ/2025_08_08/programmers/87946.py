
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for order in permutations(dungeons):
        current = k  
        count = 0      
        
        for min_r, cost in order:
            if current >= min_r:
                current -= cost  
                count += 1         
        
        answer = max(answer, count)
    
    return answer