n = int(input())

dp = [int(1e9)] * (1000001)
prev = [0] * (1000001)

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
prev[2] = 1
prev[3] = 1
prev[4] = 2  # 4는 2를 통해 오는 게 최솟값

for i in range(5, n + 1):
    # 3으로 나누어 떨어지면
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

    # 2로 나누어 떨어지면
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

    # 1을 뺀다
    if dp[i] > dp[i - 1] + 1:
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1

print(dp[n])

# 경로 추적
path = []
cur = n
while cur != 0:
    path.append(cur)
    cur = prev[cur]

print(*path)