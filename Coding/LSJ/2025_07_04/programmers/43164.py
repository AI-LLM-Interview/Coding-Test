def solution(tickets):
    """
    DFS(깊이 우선 탐색) + 스택을 이용한 항공권 경로 찾기
    
    핵심 아이디어:
    1. 가능한 모든 경로를 탐색
    2. 알파벳 순서로 우선순위를 둠
    3. 모든 티켓을 사용하는 경로만 유효
    """
    
    # 스택의 각 원소: (현재위치, 지금까지의경로, 사용된티켓인덱스들)
    stack = [("ICN", ["ICN"], set())]
    all_paths = []  # 완성된 모든 경로들을 저장
    
    # 2. DFS 탐색 시작
    while stack:
        # 스택에서 현재 상태를 꺼냄 (LIFO - Last In First Out)
        current_pos, path, used_tickets = stack.pop()
        
        # 3. 종료 조건 체크
        # 모든 티켓을 사용했다면 완성된 경로
        if len(used_tickets) == len(tickets):
            all_paths.append(path[:])  # path[:]로 복사본 저장
            continue  # 다음 경로 탐색으로
        
        # 4. 현재 위치에서 갈 수 있는 티켓들 찾기
        available_tickets = []
        for i, (start, end) in enumerate(tickets):
            # 조건: 출발지가 현재 위치이고, 아직 사용하지 않은 티켓
            if start == current_pos and i not in used_tickets:
                available_tickets.append((i, end))  # (티켓인덱스, 목적지)
        
        # 5. 알파벳 순서로 정렬 (역순)
        available_tickets.sort(key=lambda x: x[1], reverse=True)
        
        # 6. 가능한 모든 선택지를 스택에 추가
        for ticket_idx, destination in available_tickets:
            new_path = path + [destination]  # 새로운 경로 = 기존경로 + 목적지
            new_used = used_tickets | {ticket_idx}  # 집합 합집합으로 사용된 티켓 추가
            stack.append((destination, new_path, new_used))
    
    # 7. 결과 반환
    # 모든 유효한 경로 중에서 사전순으로 가장 빠른 것 반환
    return min(all_paths) if all_paths else []