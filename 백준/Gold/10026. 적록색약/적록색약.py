from collections import deque

n = int(input())

check = [[0]* (n) for _ in range(n)]
arr = [list(input()) for _ in range(n)]

def BFS(x,y):
  
    queue = deque()
    queue.append((x,y))
    check[x][y] = 1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while(len(queue) > 0):
        X,Y = queue.popleft()

        for i in range(4):
            DX = X + dx[i]
            DY = Y + dy[i]

            if (DX < n and DY < n and DX >= 0 and DY >= 0 and check[DX][DY] == 0 and arr[DX][DY] == arr[X][Y]):
                check[DX][DY] = 1
                queue.append((DX,DY))
    

total = 0
ans = 0

for i in range(n):
    for j in range(n):
        if (check[i][j] == 0):

            BFS(i,j)
                
            total += 1

check2 = [[0]* (n) for _ in range(n)]
arr2 = [['R' if cell == 'G' else cell for cell in row] for row in arr]


def BFS2(x,y):
  
    queue = deque()
    queue.append((x,y))
    check2[x][y] = 1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while(len(queue) > 0):
        X,Y = queue.popleft()

        for i in range(4):
            DX = X + dx[i]
            DY = Y + dy[i]

            if (DX < n and DY < n and DX >= 0 and DY >= 0 and check2[DX][DY] == 0 and arr2[DX][DY] == arr2[X][Y]):
                check2[DX][DY] = 1
                queue.append((DX,DY))
    
for i in range(n):
    for j in range(n):
        if (check2[i][j] == 0):
            BFS2(i,j)
            ans += 1


print(total)
print(ans)
