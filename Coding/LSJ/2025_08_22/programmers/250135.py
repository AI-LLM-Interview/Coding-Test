def solution(h1, m1, s1, h2, m2, s2):
    def count_alarms(h, m, s):
        total_seconds = h * 3600 + m * 60 + s
        
        # 초침과 분침: 1시간에 59번
        minute_meets = total_seconds * 59 // 3600
        
        # 초침과 시침: 12시간에 719번
        hour_meets = total_seconds * 719 // 43200
        
        # 0시와 12시에서 중복 제거
        overlaps = total_seconds // 43200
        
        return minute_meets + hour_meets - overlaps
    
    start_alarms = count_alarms(h1, m1, s1)
    end_alarms = count_alarms(h2, m2, s2)
    
    result = end_alarms - start_alarms
    
    # 시작 시간이 정확히 0시 또는 12시 정각이면 그 순간의 알람을 포함
    if (h1 == 0 and m1 == 0 and s1 == 0) or (h1 == 12 and m1 == 0 and s1 == 0):
        result += 1
    
    return result