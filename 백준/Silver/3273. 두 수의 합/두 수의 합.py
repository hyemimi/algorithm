n = int(input())
arr = list(map(int,input().split()))
x = int(input()) # 충족 해야 하는 합

arr.sort()

lt = 0
rt = n-1
Sum = 0
ans = 0

while (lt < rt):
    
    Sum = arr[lt] + arr[rt]

    if (Sum == x): 
        ans += 1
        lt += 1
        rt -= 1
    elif (Sum < x):
        # 목표 값보다 작으면 lt를 증가시킴
        lt += 1
    else :
        # 목표 값보다 크면 rt를 감소시킴 
        rt -= 1

    

print(ans)