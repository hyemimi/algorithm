t = int(input())

while(t > 0) :

    n = int(input())
    
    dp = [0] * 11

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    
    else :


        for i in range(4,n+1):

            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        print(dp[n])

    t -= 1