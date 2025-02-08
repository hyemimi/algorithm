from collections import deque

n,m = map(int,input().split()); # 세로, 가로

board = []

cnt = 0 # 전체 치즈 갯수

for i in range(n):
    board.append(list(map(int,input().split()))) 
    cnt += sum(board[i])

# 0이면 공기, 1이면 치즈 0인 경우에 큐에 넣어 검사 

def BFS():
    queue = deque()
    cheese = deque()
    visited[0][0] = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue.append((0,0))

    while (len(queue) > 0):
        a,b = queue.popleft()

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0<= nx <n and 0 <= ny < m and not visited[nx][ny] :
                visited[nx][ny] = 1

                if board[nx][ny] == 0 :
                    # 공기이면 탐색 범위 추가
                    queue.append((nx,ny))
                elif board[nx][ny] == 1:
                    # 치즈면 한꺼번에 녹이기 위해 큐에 저장 
                    cheese.append((nx,ny))
    
    for c,d in cheese :

        board[c][d] = 0 # 녹인 처리 (공기로 만듦)
    
    return len(cheese)
        
time = 1
while (True):

    visited = [[0] * (m) for _ in range(n)]
    meltedCheese = BFS()
    cnt -= meltedCheese # 남아 있는 치즈 갯수 계산
   

    if cnt == 0 :
        # 전부 녹임
        print(time)
        print(meltedCheese)
        break

    time += 1
