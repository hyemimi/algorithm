import math

# 칼로리의 합이 가장 큰 경우

while (True):

    n, m = input().split()
    n = int(n)
    m = int(float(m) * 100 + 0.5)

    if n == 0 and m == 0:
        break
   
    dp = [0] * (m+1)

    for i in range(n):
        c, p = input().split() # c는 칼로리, p는 가격
        c = int(c)
        p = int(float(p) * 100 + 0.5)


        for j in range(p,m+1):

            dp[j] = max(dp[j],dp[j-p] + c)
    
    print(max(dp))