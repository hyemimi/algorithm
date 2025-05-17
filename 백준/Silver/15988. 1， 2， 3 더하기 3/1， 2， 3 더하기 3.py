
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력

t = int(input())

while(t):
    t -= 1
    n = int(input())

    dp = [0] * (n+1) # dp[i]는 i를 1,2,3의 합으로 나타내는 방법의 수

    if n == 1 :
        print(1% 1000000009)
        continue

    if n == 2 :
        print(2 % 1000000009)
        continue

    if n == 3 :
        print(4 % 1000000009)
        continue

    
    dp[1] = 1
    dp[2] = 2 # 1+1, 2 --> 2개
    dp[3] = 4 # 1+1+1, 1+2, 3, 2+1 --> 4개
 

    for i in range(4,n+1):
        dp[i] = dp[i-3] % 1000000009 + dp[i-2] % 1000000009 + dp[i-1] % 1000000009
    

    print(dp[n] % 1000000009)