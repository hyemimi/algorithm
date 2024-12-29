n = int(input())



lt = 1
rt = 1
k = 0

# n을 연속된 자연수의 합으로 만드려고 할 때의 경우의 수

Sum = 0
ans = 0

while(rt <= n):
    Sum += rt

    if (Sum == n):
        # 만듦
        ans += 1
     
    
    while (Sum >= n):
        # n보다 클 때

        Sum -= lt
        lt += 1

        if (Sum == n):
        # 만듦
            ans += 1

    
    rt += 1

print(ans)