def solution(triangle):
    # 마지막에서 두 번째 줄부터 위로 올라감
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 아래 두 칸 중 큰 값을 선택해서 현재에 더함
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]  # 꼭대기 위치가 최종 최대값