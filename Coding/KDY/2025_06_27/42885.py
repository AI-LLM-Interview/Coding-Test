def solution(people, limit):
    answer =0
    
    people.sort(reverse=True)   # 정렬
    
    # print(people)
    start = 0
    end = len(people)-1
    # print(end)
    
    while start <= end :
        if people[start]+people[end] > limit:
            # print('people[start]',people[start], ' people[end]',people[end],'> limit', limit)
            answer +=1
            start +=1
        elif people[start]+people[end] <= limit:
            # print('people[start]',people[start], ' people[end]',people[end],'< limit', limit)
            answer +=1
            start +=1
            end -= 1

    return answer