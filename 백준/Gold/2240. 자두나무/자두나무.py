t, w = map(int,input().split()) # t초 동안 t개의 자두 떨어짐, w번 움직일 수 있음
fruit = []

for i in range(t):
    fruit.append(int(input()))

# 주울 수 있는 자두의 갯수 구하는 문제

dp = [[0] * (w+1) for _ in range(t+1)] # dp[i][j]는 i초에 j번 이동할 경우 최대 얻을 수 있는 자두

for i in range(1,t+1):

    for j in range(0,w+1):

        # 이동 횟수 w가 짝수이면 1번 나무 아래에 있다. current: 현재 위치
        current = 1 if j % 2 == 0 else 2 
        gain = 1 if fruit[i-1] == current else 0

        if j == 0:
            dp[i][j] = dp[i-1][j] + gain

        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + gain # 이동 하거나, 이동 안 하거나

print(max(dp[t]))

