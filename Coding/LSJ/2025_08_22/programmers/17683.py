def solution(m, musicinfos):
    answer = []
    
    # 샵을 하나의 문자로 찾기 위한 치환
    dict_ = {"C#": "H", "D#": "I", "F#":"J", "G#":"K", "A#":"L"}
    
    # 문자 치환
    for key, value in dict_.items():
        m = m.replace(key,value)
    
    for i, musicinfo in enumerate(musicinfos):
        stime, etime, title, song = musicinfo.split(",")
        
        # 문자 치환
        for key, value in dict_.items():
            song = song.replace(key,value)
        
        # 재생 시간 계산
        hour, minute = int(etime[:2]) - int(stime[:2]), int(etime[3:]) - int(stime[3:])
        played_time = 60*hour + minute
        
        # 재생된 시간이 음악 길이보다 길 때
        if played_time > len(song):
            song *= (played_time // len(song)) + 1
            
        # 재생된 시간이 음악 길이보다 짧을 때
        elif played_time < len(song):
            song = song[:played_time]
        
        # 후보 저장할 때 조건 정렬 위한 재생 시간, 순서 정보 저장
        if m in song:
            answer.append((title, played_time, i))
    
    # 재생 시간 긴 순서대로 정렬 -x[1] , 노래 순서대로 정렬 x[2]
    return_cand = sorted(answer, key = lambda x: (-x[1], x[2]))
    
    # 빈 정렬이면 "(None)" return
    return return_cand[0][0] if return_cand != [] else "(None)"