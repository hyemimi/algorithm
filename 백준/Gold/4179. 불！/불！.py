from collections import deque
import sys

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

# 불과 지훈이 방문 시간 기록
fire_visited = [[-1] * c for _ in range(r)]
jihoon_visited = [[-1] * c for _ in range(r)]

fire_queue = deque()
jihoon_queue = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            fire_queue.append((i, j))
            fire_visited[i][j] = 0
        elif board[i][j] == 'J':
            jihoon_queue.append((i, j))
            jihoon_visited[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 🔥 불 먼저 BFS
while fire_queue:
    x, y = fire_queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if fire_visited[nx][ny] == -1 and board[nx][ny] != '#':
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                fire_queue.append((nx, ny))

# 🧍‍♂️ 지훈이 BFS
def escape():
    while jihoon_queue:
        x, y = jihoon_queue.popleft()
        # 가장자리면 탈출 성공
        if x == 0 or x == r-1 or y == 0 or y == c-1:
            return jihoon_visited[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != '#' and jihoon_visited[nx][ny] == -1:
                    # 불보다 먼저 도착해야 이동 가능
                    if fire_visited[nx][ny] == -1 or jihoon_visited[x][y] + 1 < fire_visited[nx][ny]:
                        jihoon_visited[nx][ny] = jihoon_visited[x][y] + 1
                        jihoon_queue.append((nx, ny))
    return "IMPOSSIBLE"

print(escape())
