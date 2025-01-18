n,m = map(int,input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

k = int(input())


for s in range(k):
    i,j,x,y = map(int,input().split())

    ans = 0

    for a in range(i-1,n):

        if a > x-1:
            break

        for b in range(j-1,m):

            if b > y-1 :
                break 
            ans += arr[a][b]
    
    print(ans)