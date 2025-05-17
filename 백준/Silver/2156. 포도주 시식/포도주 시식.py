# 포도주를 마실 수 있는 최대 양?
# 연속 세 번은 안돼

n = int(input())

grapes = []

for i in range(n):
    grapes.append(int(input()))


dp = [0] * (n+1)


if n == 1:
    print(grapes[0])
    exit()
elif n == 2:
    print(grapes[0] + grapes[1])
    exit()

dp[0] = grapes[0] # 4
dp[1] = grapes[0] + grapes[1] # 4 + 1 = 5 
dp[2] = max(grapes[0]+grapes[2], grapes[1]+grapes[2], grapes[0]+grapes[1] )

for i in range(3,n):
    
    dp[i] = max(dp[i-1],grapes[i-1] + grapes[i] + dp[i-3], grapes[i] + dp[i-2])


print(dp[n-1])

