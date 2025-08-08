def solution(n, times):
    l = 1
    r = max(times)*n
    
    # 이진탐색
    while l <= r:
        tmp = 0
        mid = (l+r)//2
        
        for t in times:
            tmp += mid//t
            if tmp >= n:
                break
            
        if tmp >= n:
            answer = mid
            r = mid - 1
            
        else:
            l = mid+1
    
    return answer