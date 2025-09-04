from collections import deque

def solution(cacheSize, cities):
    # 캐시 크기가 0이면 모든 요청이 cache miss
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque()  # LRU 캐시를 구현하기 위한 deque
    total_time = 0
    
    for city in cities:
        # 대소문자 구분하지 않으므로 소문자로 변환
        city_lower = city.lower()
        
        # Cache Hit - 캐시에 있는 경우
        if city_lower in cache:
            # 해당 도시를 캐시에서 제거하고 맨 앞으로 이동 (가장 최근 사용)
            cache.remove(city_lower)
            cache.appendleft(city_lower)
            total_time += 1
        
        # Cache Miss - 캐시에 없는 경우
        else:
            # 캐시가 가득 찬 경우, 가장 오래된 항목(맨 뒤) 제거
            if len(cache) >= cacheSize:
                cache.pop()
            
            # 새 도시를 캐시 맨 앞에 추가
            cache.appendleft(city_lower)
            total_time += 5
    
    return total_time