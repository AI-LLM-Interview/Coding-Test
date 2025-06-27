from collections import defaultdict

def solution(genres, plays):
    genre_to_songs = defaultdict(list)
    total_plays = defaultdict(int)

    # 1. 데이터 수집
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_to_songs[g].append((i, p))
        total_plays[g] += p

    # 2. 장르 정렬 (총 재생 횟수 기준)
    sorted_genres = sorted(total_plays.keys(), key=lambda g: total_plays[g], reverse=True)

    answer = []
    for g in sorted_genres:
        # 3. 장르 내 노래 정렬: 재생 횟수 내림 + id 오름
        songs = sorted(genre_to_songs[g], key=lambda x: (-x[1], x[0]))
        # 4. 최대 두 곡 선택
        answer.extend([song[0] for song in songs[:2]])

    return answer
