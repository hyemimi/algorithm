t = int(input())

while(t):

    arr = list(map(int,input().split()))

    arr.sort(reverse=True)
    print(arr[2])

    t-=1
