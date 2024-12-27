from collections import deque

m,n = map(int,input().split())

#정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
#익을 때까지 얼마나 걸릴 것인가?
# 익은 토마토의 영향 - 인접 토마토

fruits = [list(map(int,input().split())) for _ in range(n)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]


# 익은 토마토를 기준으로 pop해서, 주변의 익지 않은 토마토들을 익게 만든다.
# 일수 계산을 위해 fruits 배열 값을 이전의 값에 합해준다. (익지 않았었으나 익은 토마토의 경우를 이때 계산 한다.)
queue = deque()
for i in range(n):
    for j in range(m):
        if fruits[i][j] == 1:
            queue.append((i, j))  # 익은 토마토의 좌표

def BFS():
  
    count = 0

    while(len(queue) > 0):
        X,Y = queue.popleft()

        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]

            if (0<= nx < n and 0<=ny <m and fruits[nx][ny] == 0):
                queue.append((nx,ny))
                fruits[nx][ny] = fruits[X][Y] + 1
                count = max(count, fruits[nx][ny]) # 최대 일수

    return count


result = BFS()
isNotCompleted = False

# 익지 않은 토마토 검사 (0)
for row in fruits:
    if 0 in row: 
        print(-1)
        isNotCompleted = True
        break

# 모두 익었다면 결과 출력 (최대 일수 - 1: 익은 상태 1에서부터 계속 더해 1부터 시작했으므로)

if (isNotCompleted==False) : print( result - 1 if result > 0 else 0) # 0인 경우는 처음부터 다 익은 상태 