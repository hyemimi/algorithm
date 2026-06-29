from collections import deque

def solution(maps):
    limit = int(1e9)
    
    answer = limit
    n = len(maps)
    m = len(maps[0])
    
    visit = [[False] * (m+1) for _ in range(n+1)]
    queue = deque([(0,0,1)])
    visit[0][0] = True
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while(queue):
        x, y, cnt = queue.popleft()
        
        if x == n-1 and y == m-1:
            # 도착
            answer = min(answer, cnt)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == False and maps[nx][ny] == 1:
                visit[nx][ny] = True
                queue.append((nx,ny, cnt+1))
    
    if answer == limit :
        return -1 
    else:
        return answer

