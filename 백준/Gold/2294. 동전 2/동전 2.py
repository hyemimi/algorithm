n, k = map(int,input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

dp = [1e9] * (k+1)

dp[0] = 0


for coin in coins:

    for i in range(coin,k+1):
        dp[i] = min(dp[i-coin]+1,dp[i])

print(dp[k] if dp[k] != 1e9 else -1)


