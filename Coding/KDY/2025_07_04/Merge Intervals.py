class Solution(object):
    def merge(self, intervals):

        intervals.sort()
        answer = []

        # 입력 최소값 0이므로 
        x = -1
        y = -1

        for interval in intervals:
            # print('input', interval)

            start = interval[0]
            end = interval[1]
            
            if x == -1 and y == -1:
                x= start
                y= end

            elif start <= y :
                y = max(y,end)

            elif y < start:
                answer.append([x,y])
                x = start
                y = end

            # print('answer',answer)
            # print('-'*20)

        answer.append([x, y])
        # print(answer)
        return answer