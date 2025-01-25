n = int(input())

# 돌 1,3,4개까지 가져갈 수 있음. 상근이부터 번갈아
# 이기는 경우 : 상근 SK 창영 CY

dp = [0] * (n+1)

# i는 게임 횟수 
# dp는 상근이가 이기면 1, 창영이 이기면 2
# dp[1] = 1 dp[2] = 2 dp[3] = 1 dp[4] = 1 / dp[5] = 2 dp[5] = 2 

dp[1] = 1

if n > 1 :
    dp[2] = 2

if n > 2 :
    dp[3] = 1

if n > 3 :
    dp[4] = 1


for i in range(5,n+1):

    if dp[i-1] == 2 or dp[i-3] == 2 or dp[i-4] == 2:
        # i-1, i-3, i-4에서 창영이가 이기면 다음 경기는 무조건 상근이가 이김
        dp[i] = 1
    else :
        dp[i] = 2



if dp[n] == 1 :
    print("SK")
else :
    print("CY")
