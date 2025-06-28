def solution(edges):
    answer = []
    for a, b in edges:
        outdegree[a] += 1
        indegree[b] += 1
    
    generator, donut, stick, eight = 0, 0, 0, 0
    
    all_nodes = set(indegree.keys()).union(outdegree.keys())
    return answer