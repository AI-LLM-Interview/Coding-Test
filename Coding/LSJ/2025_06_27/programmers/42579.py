def solution(genres, plays):
    genre_sum = {}
    for i, genre in enumerate(genres):
        if genre not in genre_sum:
            genre_sum[genre] = 0
        genre_sum[genre] += plays[i]
        
    sort_genres = sorted(genre_sum.keys(), key=lambda x: genre_sum[x], reverse=True)
    
    songs = {}
    for i, genre in enumerate(genres):
        if genre not in songs:
            songs[genre] = []
        songs[genre].append((plays[i], i))
        
    for genre in songs:
        songs[genre].sort(key=lambda x: (-x[0], x[1]))    
    
    answer = []
    for genre in sort_genres:
        song = songs[genre]
        for i in range(min(2, len(song))):
            answer.append(song[i][1])
            
    return answer