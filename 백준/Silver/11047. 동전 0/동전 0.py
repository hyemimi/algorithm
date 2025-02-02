n,k = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)


ans = 0

for i in range(n):

    if k==0 : break

    elif arr[i] <= k:

        ans += k // arr[i] # 동전 갯수 -> 몫
        k = k % arr[i] # 남은 돈 -> 나머지 



print(ans)