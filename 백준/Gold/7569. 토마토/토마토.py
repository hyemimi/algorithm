from collections import deque

m,n,h = map(int,input().split())

#정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
#익을 때까지 얼마나 걸릴 것인가?
# 익은 토마토의 영향 - 인접 토마토

# 3차원 리스트로 토마토 상자 초기화
fruits = []
for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    fruits.append(layer)

# 3차원 컨트롤 상,하,좌,우,위,아래
dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,-1,1]


# 익은 토마토를 기준으로 pop해서, 주변의 익지 않은 토마토들을 익게 만든다.
# 일수 계산을 위해 fruits 배열 값을 이전의 값에 합해준다. (익지 않았었으나 익은 토마토의 경우를 이때 계산 한다.)
queue = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if fruits[z][x][y] == 1:
                queue.append((z,x,y))  # 익은 토마토의 좌표

def BFS():
  
    count = 0

    while(len(queue) > 0):
        Z,X,Y = queue.popleft()

        for i in range(6):
           
           
            nz = Z + dz[i]
            nx = X + dx[i]
            ny = Y + dy[i]

            if (0<=nz<h and 0 <= nx < n and 0 <= ny < m and fruits[nz][nx][ny] == 0):
                queue.append((nz,nx,ny))
                fruits[nz][nx][ny] = fruits[Z][X][Y] + 1



BFS()
isNotCompleted = False

# 익지 않은 토마토 검사 (0) & 최대 일수 계산 
result = 0
for height in fruits:
    for row in height:
        if 0 in row:  
            print(-1) # 익지 않은 토마토가 있으면 -1 출력
            exit() 
        result = max(result, max(row))

# 모두 익었다면 결과 출력 (최대 일수 - 1: 익은 상태 1에서부터 계속 더해 1부터 시작했으므로)

if (isNotCompleted==False) : print( result - 1 if result > 0 else 0) # 0인 경우는 처음부터 다 익은 상태 