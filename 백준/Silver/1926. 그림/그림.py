from collections import deque;

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]



def BFS(x,y):

    queue = deque()

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue.append((x,y))
    cnt = 1 # 그림 넓이이

    visited[x][y] = 1 # 처음 방문 처리


    while (len(queue) > 0):
        k,s = queue.popleft()

        for i in range(4):

            toX = k + dx[i]
            toY = s + dy[i]

            if ( toX < n and toY < m and toX >= 0 and toY >= 0 and arr[toX][toY] == 1 and visited[toX][toY] != 1) :
                queue.append((toX,toY))
                visited[toX][toY] = 1
                cnt += 1

    return cnt

result = []
answer = 0

for i in range(n):
    for j in range(m):
        if (visited[i][j] != 1 and arr[i][j] == 1):
            # 방문하지 않았고, 그림 영역이면 BFS 수행행
            answer = BFS(i,j)
            result.append(answer)





print(len(result))

ans = 0
for i in result:
    if (i > ans):
        ans = i

print(ans)