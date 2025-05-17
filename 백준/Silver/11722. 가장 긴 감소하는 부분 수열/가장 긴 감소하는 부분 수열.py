n = int(input())
arr = list(map(int,input().split()))

# 선택 하느냐, 안 하느냐로

dp = [1] * (n+1) # dp[i]는 i-1번째 요소까지의 가장 긴 감소하는 부분 수열의 길이

for i in range(n):
    for j in range(i):

        if arr[j] > arr[i]:

            dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))