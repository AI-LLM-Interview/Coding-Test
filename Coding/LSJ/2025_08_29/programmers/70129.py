def solution(s):
    cnt = 0
    zeros = 0
    while s != '1':
        zeros += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
        cnt += 1
    return [cnt, zeros]