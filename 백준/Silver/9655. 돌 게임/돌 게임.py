n = int(input())

# 1개 혹은 3개 가져갈 수 있음
# dp[n]이 홀수이면 상근이가 이김 'SK'  

dp = [0] * (n+1)


for i in range(1,n+1):
    if i < 3:
        dp[i] = dp[i-1] + 1
    else :
        dp[i] = min(dp[i-1] + 1, dp[i-3]+1) # 1개 집거나, 3개 집거나


if dp[n] % 2 == 0 :
    print('CY')
else:
    print('SK')