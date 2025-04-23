from collections import deque

n,m,k = map(int,input().split())
board = [[0] * (m+1)  for _ in range(n+1)]


for i in range(k):
    r,c = map(int,input().split())
    board[r][c] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]



# 연속 구간 크기 출력하기
def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    board[x][y] = 0
    cnt = 1

    while(len(queue) > 0):
    
        a,b = queue.popleft()

        for i in range(4):
            na = dx[i] + a
            nb = dy[i] + b

            if 1<=na<=n and 1<=nb<=m and board[na][nb] == 1 :
                board[na][nb] = 0
                queue.append((na,nb))
                cnt += 1
   
    return cnt

ans = 1
 
for i in range(1,n+1):
    for j in range(1,m+1):
        if board[i][j] == 1:
            ans = max(BFS(i,j),ans)

print(ans)