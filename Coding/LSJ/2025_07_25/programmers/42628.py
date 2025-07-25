import heapq

def solution(operations):
    min_q = []
    max_q = []
    
    for operation in operations:
        command = operation.split()[0]
        value = int(operation.split()[1])
        
        if command == "I":
            heapq.heappush(min_q, value)
            heapq.heappush(max_q, -value)
        
        elif command == "D":
            if value == 1:
                if max_q:
                    max_val = -heapq.heappop(max_q)
                    min_q.remove(max_val)
                    heapq.heapify(min_q)
            elif value == -1:
                if min_q:
                    min_val = heapq.heappop(min_q)
                    max_q.remove(-min_val)
                    heapq.heapify(max_q)
    
    if not min_q or not max_q:
        return [0, 0]
    else:
        return [-max_q[0], min_q[0]]