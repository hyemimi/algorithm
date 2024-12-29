import sys
T = int(input())


while (T > 0):

    
    n, x = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()

    lt = 0
    rt = n-1
    minSum = sys.maxsize
    ans = 0

    while (lt < rt) :
        Sum = arr[lt] + arr[rt]

        if (abs(x - Sum) == minSum):
            ans += 1

        elif (abs(x - Sum) < minSum):
            ans = 1
            minSum = abs(x-Sum)
        
        if (Sum < x):
            # 작으면 lt += 1
            lt += 1
        else :
            # 큰 경우
            rt -= 1 
        
    print(ans)
    T -= 1


