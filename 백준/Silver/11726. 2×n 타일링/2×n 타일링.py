n = int(input())

dp = [0] * 1001

dp[1] = 1 # 2x1 타일 사용
dp[2] = 2 # 1x2 2개 / 2x1 2개 총 경우의 수 2개

# 1x2 , 2x1 타일 존재 
for i in range(3,n+1):

    dp[i] = (dp[i-1] + dp[i-2]) %  10007


print(dp[n])