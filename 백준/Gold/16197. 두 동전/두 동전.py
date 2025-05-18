# 두 동전 중 하나만 떨어뜨려야 함
# 최소 횟수 구하기
# 두 동전 중 하나만을 떨어뜨릴 수 없거나, 10번 보다 많이 이동해야 하면 -1 출력 

n,m = map(int,input().split())
board = []

for i in range(n):
    board.append(list(input().rstrip()))

# #: 벽 (이동할 수 없음)
# .: 빈칸 (이동할 수 있음)
# o: 동전

coin = []

for i in range(n):
    for j in range(m):

        if board[i][j] == 'o':
            # 동전 위치
            coin.append((i,j))

from collections import deque

queue = deque()
queue.append((coin[0],coin[1],0)) # 코인 위치 

dx = [-1,0,1,0]
dy = [0,1,0,-1]


while (len(queue)>0):
    temp = queue.popleft()
    x1,y1 = temp[0]
    x2,y2 = temp[1]
    cnt = temp[2]

    if cnt >= 10:
        print(-1)
        break

    for i in range(4):

        # 이동 시 두 동전이 다 떨어지는 경우
        if ( x1+dx[i] < 0 or x1+dx[i] >= n or y1+dy[i] < 0 or y1+dy[i] >= m ) and  ( x2+dx[i] < 0 or x2+dx[i] >= n or y2+dy[i] < 0 or y2+dy[i] >= m):
            continue
    
        # 이동 시 하나의 동전만 떨어지는 경우 
        if ( x1+dx[i] < 0 or x1+dx[i] >= n or y1+dy[i] < 0 or y1+dy[i] >= m  ) or ( x2+dx[i] < 0 or x2+dx[i] >= n or y2+dy[i] < 0 or y2+dy[i] >= m ):
            print(cnt+1)
            exit()

        # 그냥 이동
        if 0<=x1+dx[i]<n and 0<=x2+dx[i]<n and 0<=y1+dy[i]<m and 0<=y2+dy[i]<m :
            
            next1 = (x1+dx[i],y1+dy[i])
            next2 = (x2+dx[i],y2+dy[i])

            if board[x1+dx[i]][y1+dy[i]] == '#' :
                next1 = (x1,y1)
            
            if board[x2+dx[i]][y2+dy[i]] == '#':
                next2 = (x2,y2)

            queue.append((next1,next2,cnt+1))

   