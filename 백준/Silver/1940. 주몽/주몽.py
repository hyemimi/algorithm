# M이 되면 갑옷을 만들 수 있음
# 갑옷을 만드는 경우의 수?
n = int(input())
m = int(input())
arr = list(map(int,input().split()))

arr.sort() # 정렬
lt = 0
rt = n-1
Sum = 0
ans = 0

while (lt < rt):
    
    temp = arr[lt] + arr[rt] # 두 개 재료의 합

    if (temp == m):
        ans += 1
    
    if (temp > m):
        # m을 초과해버리니 더 작게 만듦
        rt -= 1
    else :
        # 작으니까 더해줌 
        lt += 1
    
    

print(ans)