n, m = map(int, input().split())
arr = []

# 모든 학생 (능력치, 반 번호) 저장
for c in range(1, n+1):
    a = map(int, input().split())
    arr.extend(zip(a, [c]*m))

# 능력치 기준 오름차순 정렬
arr.sort()

dic = {}  # 구간 내 반 번호별 등장 횟수
result = 100000000  # 최소 차이 초기값 설정
l = 0  # 왼쪽 포인터

# 투포인터 슬라이딩 윈도우 탐색
for r in range(len(arr)):
    ability, cls = arr[r]
    dic[cls] = dic.get(cls, 0) + 1  # 구간 내 해당 반 등장 횟수 추가

    # 모든 반이 포함될 때 구간 축소 시도
    while len(dic) == n:
        diff = arr[r][0] - arr[l][0]  # 구간 내 최댓값 - 최솟값
        result = min(result, diff)  # 최소 차이 갱신

        # 왼쪽 포인터 축소, 해당 반 등장 횟수 감소
        left_cls = arr[l][1]
        cnt[left_cls] -= 1
        if dic[left_cls] == 0:
            del dic[left_cls]
        l += 1
