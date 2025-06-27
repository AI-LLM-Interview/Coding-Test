from collections import defaultdict

def solution(edges):
    indeg = defaultdict(int)
    outdeg = defaultdict(int)

    # 차수 계산
    for u, v in edges:
        outdeg[u] += 1
        indeg[v] += 1

    root = None
    bar = eight = 0

    # 모든 노드 확인
    nodes = set(indeg) | set(outdeg)
    for node in nodes:
        i = indeg[node]
        o = outdeg[node]
        if i == 0 and o >= 2:
            root = node
        elif i >= 1 and o == 0:
            bar += 1
        elif i >= 2 and o == 2:
            eight += 1

    # 도넛 개수 계산
    donut = outdeg[root] - bar - eight

    return [root, donut, bar, eight]
