def solution(phone_book):
    answer = True
    dic = {}
    for num in phone_book:
        dic[num] = 1
        # print('num: ',num)
        # print('dic[num]: ',dic[num])
    
    for num in phone_book:
        for i in range(1, len(num)):
            print('num[:i]: ', num[:i],'  dic: ', dic)
            if num[:i] in dic :
                return False
    
    
    return answer