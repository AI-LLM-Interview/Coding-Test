from operator import itemgetter
# data = [(500, 0), (800, 3), (150, 2)]
# data.sort(key=itemgetter(0))

def solution(genres, plays):
    answer = []
    total_count = {}    # 장르별 총 재생수
    genre_song = {}     # 장르가 같은 (재생수, 곡번호)
    
    # dict 정의
    for i, (g,p) in enumerate(zip(genres, plays)):
        if g not in total_count:
            total_count[g] = p
            genre_song[g] = []
        else:
            total_count[g] += p
        
        genre_song[g].append((p,i))
    
    # print(genre_song)
    # print(total_count)
    
    # 정렬
    sort_count = sorted(total_count.items(), key=itemgetter(1), reverse=True)
    # print(sort_count)
    
    # 총 곡수가 가장 큰 장르
    for g , k in sort_count: #('pop', 3100), ('classic', 1450)
        sort_song = sorted(genre_song[g], key=itemgetter(0), reverse=True)
        # print(sort_song[:2])
        for song in sort_song[:2]:
            answer.append(song[1])
    
    return answer