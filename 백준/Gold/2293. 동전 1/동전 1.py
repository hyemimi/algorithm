n, k = map(int,input().split()) # n가지 종류 동전, 합이 k원이 되도록 설정
coins = [] # 동전의 가치를 나타냄

for i in range(n):
    coins.append(int(input()))

dp = [0] * (10001)

dp[0] = 1

for coin in coins:

    for i in range(coin,k+1):
        dp[i] += dp[i-coin]

print(dp[k])
