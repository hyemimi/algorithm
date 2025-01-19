n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]  # arr 복사 


for i in range(1, n):
    # arr[i-1]까지 검사 
    for j in range(i):
        if arr[j] < arr[i]:  # 증가 검사 
            dp[i] = max(dp[i], dp[j] + arr[i])


print(max(dp))