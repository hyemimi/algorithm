from collections import deque

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]


def BFS(x,y,height):
    queue = deque()
    check[x][y] = 1
    queue.append((x,y))

    while (len(queue) > 0) :
        a,b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if  0<=nx<n and 0<=ny<n and check[nx][ny] == 0 and arr[nx][ny] > height :
                check[nx][ny] = 1
                queue.append((nx,ny))

max_height = max(map(max,arr)) # 최대 높이
cnt = 0

for k in range(0,max_height):
    check = [[0] * n for _ in range(n)]
    temp = 0

    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and arr[i][j] > k:
                # 잠기지 않는 영역 검사 시작
                BFS(i,j,k)
                temp += 1
    
    cnt = max(temp,cnt)

print(cnt)