from collections import deque

def solution(land):
    answer = 0
    
    # 0이면 빈 땅, 1이면 석유가 있는 땅
    n = len(land)
    m = len(land[0])
    
    # 연결된 것 세기. 가장 많은 -> BFS
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    visit = [[0] * (m+1) for _ in range(n+1)]
    
    def BFS(i,j):
        
        queue = deque([(i,j)])
        cnt = 1
        visit[i][j] = 1
        cols = {j}

        while(queue):
            x,y = queue.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if (0<=nx<n and 0<=ny<m and land[nx][ny] == 1 and visit[nx][ny] ==0):
                    # 경계선 테스트 및 석유, 중복 방문 점검
                    cnt += 1
                    visit[nx][ny] = 1
                    queue.append((nx,ny))
                    cols.add(ny)
        
        return cnt,cols      
        
    oil = [0] * m
    
    # 시추관으로 몇 개의 석유를 뽑아낼 수 있는지 카운트
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visit[i][j] != 1:
                cnt, cols = BFS(i, j)

                for col in cols:
                    oil[col] += cnt
        
    
    return max(oil)