# 조이스틱 문제

# 이동 최솟값 계산
# JAZZ 라면 'A'AAA -> 'J'AAA -> JAA'Z' -> JA'Z'Z
# BZAZAAAAAZZAZ 라고 하면 ZZAZ'B'ZAZ AAAAA  4<-B->3
# 좌우 최소값: 4 + 3 + min(3,4) 또는 한 방향으로 쭉 이동하는 경우 = 13 - 1

def solution(name):

    answer = 0
    length = len(name)          # 글자 길이
    min_move = len(name) - 1    # 한 방향으로만 이동하는 경우
    
    
    for i, text in enumerate(name):    # 인덱스와 문자 순회
        
        # 상하 이동 수 계산
        answer += min(ord(text) - ord('A'),
                      ord('Z') - ord(text) + 1 )

        # 연속된 A 위치 (i~ii) 계산
        ii = i + 1
        while ii < len(name) and name[ii] =='A':
            ii += 1

        front = i
        back = len(name)-ii

        # 좌우 이동 수 계산
        min_move = min(min_move,
                       front + back + min(front, back))
        
    return answer + min_move