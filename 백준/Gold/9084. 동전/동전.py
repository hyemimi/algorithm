t = int(input())

while(t):

  
    n = int(input()) # 동전 가짓수
    dp = [0] * (10001)
    dp[0] = 1

   
    coins = list((map(int,input().split())))
    

    m = int(input()) # 만들어야 할 금액 



    for coin in coins:

        for i in range(coin,m+1):
            dp[i] += dp[i-coin] 
    
    print(dp[m])





    t-= 1