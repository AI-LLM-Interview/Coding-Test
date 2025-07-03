def solution(name):
    answer = 0
    length = len(name)
    min_move = len(name) - 1
    
    
    for i, n in enumerate(name):
        answer += min(ord(n) - ord('A'),ord('Z')-ord(n)+1)
        ii = i + 1
        while ii < len(name) and name[ii] =='A':
            ii += 1
        front = i
        back = len(name)-ii
        min_move = min(min_move, front+back+min(front,back))
    return answer + min_move