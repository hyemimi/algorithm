import heapq
from collections import deque

m, n = map(int,input().split()) 
board = [list(map(int, input())) for _ in range(n)] # n * m
check = [[0] * (m) for _ in range(n)]

pq = []

# 첫 시작 
heapq.heappush(pq,(0,0,0)) # count, x, y

check[0][0] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while (len(pq) > 0):
    count,x,y = heapq.heappop(pq)

    if x == n-1 and y == m-1 :
        print(count)
        break

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 :

            check[nx][ny] = 1

            if board[nx][ny] == 1 :
                # 벽을 부셔야 하는 경우 
                heapq.heappush(pq,(count + 1,nx,ny))
            else :
                # 벽 부시지 x
                heapq.heappush(pq,(count,nx,ny))
            

