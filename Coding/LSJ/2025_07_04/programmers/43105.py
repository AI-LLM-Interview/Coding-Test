def solution(triangle):
    sum_tri = [row[:] for row in triangle]
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            sum_tri[i+1][j] = max(triangle[i+1][j] + sum_tri[i][j], sum_tri[i+1][j])
            
            if j+1 < len(triangle[i+1]):
                sum_tri[i+1][j+1] = max(sum_tri[i+1][j+1], triangle[i+1][j+1] + sum_tri[i][j])
                
    return max(sum_tri[-1])