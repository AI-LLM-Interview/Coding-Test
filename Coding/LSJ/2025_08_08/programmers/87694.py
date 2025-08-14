def solution(rectangle, characterX, characterY, itemX, itemY):
    
    board = [[0] * 100 for _ in range(100)]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if i == x1 or i == x2 or j == y1 or j == y2:
                    if board[i][j] == 0:
                        board[i][j] = 2
                else:
                    board[i][j] = 1
    return answer