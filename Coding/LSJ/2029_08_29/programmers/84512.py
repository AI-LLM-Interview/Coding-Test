def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(word)):
        n_sum = 0
        for j in range(0, 5-i):
            n_sum += 5 ** j
        answer += n_sum * arr.index(word[i])+1
        
    return answer