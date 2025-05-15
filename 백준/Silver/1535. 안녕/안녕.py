n = int(input())
lost = list(map(int,input().split()))
happy = list(map(int,input().split()))

# 체력 100, 기쁨 0
# 0이나 음수가 되면 죽음
# 최대 기쁨 구하기

dp = [0]* (101) # dp[i] 체력이 i 일 때 얻을 수 있는 최대 기쁨


for i in range(n):

    a = lost[i]
    b = happy[i]

    for j in range(100,a-1,-1):

        if 0 <j-a <= 100:

            dp[j] = max(dp[j], dp[j-a] + b)

print(max(dp))