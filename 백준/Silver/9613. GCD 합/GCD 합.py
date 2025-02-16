import math

t = int(input())

for i in range(t):
    arr = list(map(int,input().split()))

    n = arr[0]

    ans = 0

    for j in range(1,n+1):
        for k in range(j+1,n+1):
            ans += math.gcd(arr[j],arr[k])
    print(ans)