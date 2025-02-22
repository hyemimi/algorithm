from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

# 방문 여부: visited[x][y][z] -> (x,y) 위치에 z(0=벽 안 부숨, 1=벽 부숨) 상태로 도착했는지
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

# 상하좌우 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS():
    queue = deque()
    queue.append((0, 0, 0, 1))  # x, y, 벽을 부쉈는지 여부(0 or 1), 이동 횟수
    visited[0][0][0] = 1  # 시작점 방문 처리

    while queue:
        x, y, wall, cnt = queue.popleft()

        # 목적지에 도착
        if x == n-1 and y == m-1:
            print(cnt)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 확인
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 없고, 아직 방문하지 않은 경우
                if board[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = 1
                    queue.append((nx, ny, wall, cnt+1))
                # 벽이 있고, 벽을 부순 적이 없는 경우
                elif board[nx][ny] == 1 and wall == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = 1
                    queue.append((nx, ny, 1, cnt+1))

    # 목적지에 도달할 수 없는 경우
    print(-1)

BFS()