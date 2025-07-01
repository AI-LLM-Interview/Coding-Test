def solution(people, limit):
    people.sort()
    
    left = 0 
    right = len(people)
    answer = 0
    
    while left <= right+1:
        if people[left] + people[right+1] <= limit:
            left += 1
        
        right -= 1
        answer += 1
    
    return answer