from collections import deque

m,n,k = map(int,input().split())
target = []

# 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값
# 직사각형 좌표 방문 처리 찍고
# 연결 영역 구하는 문제
# BFS로 풀기

visited = [[0] * (n+1) for _ in range(m+1)]

# 직사각형 해당 방문 처리
for i in range(k):
    leftX, leftY, rightX, rightY = map(int,input().split())

    visited[leftY][leftX] = 1
    for j in range(leftY, rightY):
        for i in range(leftX,rightX):
            visited[j][i] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    global visited
    visited[x][y] = 1
    ans = 1

    while(len(queue) > 0):
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < m and 0 <= ny <n and visited[nx][ny] != 1:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                ans += 1
    
    return ans

ans = 0
each = []

for i in range(m):
    for j in range(n):

        if visited[i][j] == 0:
            cnt = BFS(i,j) # 넓이
            each.append(cnt)
            ans += 1  # 나뉘어진 영역 갯수

print(ans)
each = sorted(each)
for ele in each:
    print(ele, end=" ")
