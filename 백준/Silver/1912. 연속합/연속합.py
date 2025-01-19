n = int(input())
arr = list(map(int,input().split()))

# 연속된 가장 큰 합 구하기 
dp = arr[:]

dp[0] = arr[0]

for i in range(1,n):
        
    dp[i] = max(dp[i], dp[i-1] + arr[i])


print(max(dp))