n, m = map(int, input().split())
r, c, d = map(int, input().split())

# 방 상태 입력받기
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# shift 좌표
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 전환 함수
def turn_left():
    global d
    d = (d - 1) % 4  # 반시계 방향으로 회전 (북 → 서 → 남 → 동 순서)

# 청소 여부 체크 배열
check = [[0] * m for _ in range(n)]
check[r][c] = 1  # 시작 위치 청소
count = 1

while (True):
    turned = 0  # 방향 전환

    for _ in range(4):  # 4방향 탐색
        turn_left()
        nx, ny = r + dx[d], c + dy[d]

        # 이동 가능 
        if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0 and board[nx][ny] == 0:
            check[nx][ny] = 1
            r, c = nx, ny
            count += 1
            turned = 1
            break

    # 이동하지 못함 
    if turned == 0:
        # 후진
        nx, ny = r - dx[d], c - dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            r, c = nx, ny
        else:
            break  # 작동 멈춤

print(count)