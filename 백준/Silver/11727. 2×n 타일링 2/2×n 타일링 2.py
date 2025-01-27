n = int(input())

dp = [0] * 1001

# 1×2, 2×1과 2×2 타일링
dp[1] = 1 # 2x1 타일 사용
dp[2] = 3  # 2x1 타일 2 개 사용 / 1x2 타일 2개 / 2x2 타일 1개 => 총 3개 경우

for i in range(3,n+1):

    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[n])