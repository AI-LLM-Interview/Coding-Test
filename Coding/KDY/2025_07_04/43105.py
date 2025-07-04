def solution(triangle):
    dic= {}

    for i in range(len(triangle)-2, -1, -1):
        # print(i)
        for j in range(len(triangle[i])):
            # print(i,j)
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            print(triangle[i][j])
            dic[(i,j)] = triangle[i][j] 
    
    return triangle[0][0]