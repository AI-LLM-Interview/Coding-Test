import heapq

def solution(jobs):
    job_list = []
    for i, (req_time, duration) in enumerate(jobs):
        job_list.append([i, req_time, duration])
    
    job_list.sort(key=lambda x: x[1])
    
    time = 0
    i = 0
    queue = []
    total_turnaround = 0
    
    while i < len(job_list) or queue:
        while i < len(job_list) and job_list[i][1] <= time:
            num, req_time, duration = job_list[i]
            heapq.heappush(queue, (duration, req_time, num))
            i += 1
        
        if queue:
            duration, req_time, num = heapq.heappop(queue)
            time += duration
            turnaround_time = time - req_time
            total_turnaround += turnaround_time
        else:
            time = job_list[i][1]
    
    return total_turnaround // len(jobs)
