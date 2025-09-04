def solution(scores):
    answer = 0
    wan = scores[0]
    scores.sort(key = lambda x : (-x[0], x[1]))
    maxscore = 0
    for score in scores:
        if wan[0] < score[0] and wan[1] < score[1]:
            return -1
        if maxscore <= score[1]:
            maxscore = score[1]
            if wan[0] + wan[1] < score[0] + score[1]:
                answer += 1
    return answer + 1