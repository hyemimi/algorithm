n = int(input())

arr = list(map(int,input().split()))

# 1 2 3 3 4

arr.sort()


for i in range(1,n):

    arr[i] = arr[i-1] + arr[i]

print(sum(arr))