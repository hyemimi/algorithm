
n = int(input())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))

# 현재 칸에 적힌 수 만큼 아래, 오른쪽만 점프
# 0은 막힌 부분
# 왼쪽 위 -> 오른쪽 아래로 향하는 경로의 개수를 구함

dp = [[0] * (n) for _ in range(n)] 
dp[0][0] = 1

for i in range(n):
    for j in range(n):

        if i == n-1 and j == n-1:
            break

        jump = board[i][j]

        if jump == 0:
            continue

        if 0<= i+jump < n:
            dp[i+jump][j] += dp[i][j]
        
        if 0<= j+jump < n:
            dp[i][j+jump] += dp[i][j]
print(dp[n-1][n-1])