n, m = map(int,input().split()) # 연속 m일까지 일할 수 있음

arr = list(map(int,input().split()))

ans = 0

for i in range(0,m):

    ans += arr[i]


max_profit = ans

for i in range(m,n):

    ans = ans - arr[i-m] + arr[i]
    

    max_profit = max(max_profit,ans)



print(max_profit)