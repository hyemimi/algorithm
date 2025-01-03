# N 명이 뭉쳐있을 때 N^2 위력
# 우리팀 -> w
# 가로크기 N, 세로크기 M
from collections import deque
n,m = map(int,input().split())
arr = [list(input()) for _ in range(m)]
checkw = [[False] * (n) for _ in range(m) ]
checkb = [[False] * (n) for _ in range(m) ]

# 우리팀 모여있는 병사 카운트
def BFSW(i,j):

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    checkw[i][j] = True
    queue= deque()
    queue.append((i,j))

    count = 1

    while (len(queue) > 0) :
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <m and 0 <= ny <n and checkw[nx][ny] == False and arr[nx][ny] == 'W':
                queue.append((nx,ny))
                checkw[nx][ny] = True
                count += 1
    return count

# 상대팀 모여 있는 병사 카운트 
def BFSB(i,j):

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    checkb[i][j] = True
    queue= deque()
    queue.append((i,j))

    count = 1

    while (len(queue) > 0) :
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <m and 0 <= ny <n and checkb[nx][ny] == False and arr[nx][ny] == 'B':
                queue.append((nx,ny))
                checkb[nx][ny] = True
                count += 1
    return count


whiteSum = 0
blueSum = 0

# 우리팀 
for i in range(m):
    for j in range(n):
        if checkw[i][j] == False and arr[i][j] == 'W':
            result = BFSW(i,j)
            whiteSum += result**2

# 상대팀 
for i in range(m):
    for j in range(n):
        if checkb[i][j] == False and arr[i][j] == 'B':
            result = BFSB(i,j)
            blueSum += result**2



print(whiteSum, blueSum)