from collections import deque

n,m,k = map(int,input().split())

board = []


for i in range(n):
    board.append(list(map(int,input().strip())))

visited = [[[0]* (k+1) for _ in range(m)]  for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS():

    visited[0][0][0] = 1
    queue = deque()
    queue.append((0,0,0,1))

    while ( len(queue) > 0):
        x,y,z,cnt = queue.popleft()


        if x == n-1 and y == m-1 :
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < m :

                # 방문하지 않았고, 갈 수 있는 길이면
                if board[nx][ny] == 0 and visited[nx][ny][z] == 0 :
                    visited[nx][ny][z] = 1
                    queue.append((nx,ny,z,cnt+1))
                
                # 벽을 부숨
                elif board[nx][ny]== 1 and z < k and visited[nx][ny][z+1] == 0 :
                    visited[nx][ny][z+1] = 1

                    queue.append((nx,ny,z+1,cnt+1))
    
    return -1

print(BFS())