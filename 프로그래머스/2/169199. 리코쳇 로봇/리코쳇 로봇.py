from collections import deque

def solution(board):
    answer = int(1e9)
    n = len(board)
    m = len(board[0])
    
    # 가중치 없는 최단거리 -> BFS
    # R은 시작점, D는 장애물, G는 목표 지점
    # 한 방향으로 계속 미끄러짐.
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = deque()
    check = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n):
        board[i] = list(board[i])
        for j in range(m):
            if board[i][j] == 'R':
                # 시작점
                queue.append((0,i,j))
                check[i][j] = 1
            elif board[i][j] == 'G':
                # 도착점
                end = (i,j)
    
    while(queue):
        cnt, x, y = queue.popleft()
        
        if (x,y) == end:
            return cnt   
        
        for i in range(4):
            nx = x
            ny = y
            
            while True:
                # 장애물이나 가장자리에 도달해 이동할 수 없을 때까지 한 방향으로 계속 미끄러짐
                tx = nx + dx[i]
                ty = ny + dy[i]
                
                if  tx < 0 or tx >= n or ty < 0 or ty >= m or board[tx][ty] == 'D':
                    break
                    
                nx, ny = tx, ty
            
            if check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append((cnt+1, nx, ny))
                
            
    

    
    return -1