# N+1 부터는 회사에 없음
# 최대 수익 구하기

n = int(input())
arr = []

for i in range(n):
    t,p = map(int,input().split())
    arr.append((t,p)) # t는 기간, p는 이익

dp = [0] * (n+2) # dp[i]는 i일까지  얻을 수 있는 최대 이익

for i in range(1,n+1):

    t, p = arr[i-1][0], arr[i-1][1]

    dp[i+1] = max(dp[i], dp[i+1]) # 상담 안 함 = 이전 날짜와 같은 최대 이익

    if i+t-1 <= n :
        dp[i+t] = max(dp[i+t], dp[i] + p)


print(max(dp))