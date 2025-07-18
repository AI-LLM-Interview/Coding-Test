def solution(n,a,b):
    answer = 0
    # 리스트로 만듦
    a = a-1
    b = b-1
    
    lst = [0] * n
    lst[a] = 1
    lst[b] = 1
    # print(lst)
    # print(list(range(0,n,2)))
    # 두개씩 더함
    new = []
    while 2 not in lst:
        answer += 1
        for i in range(0,len(lst),2):
            new.append(lst[i]+lst[i+1])
            # print(new)
        lst = new
        new =[]

    return answer