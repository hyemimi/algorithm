n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

dict = {}

# O(n^2)
for i in range(n):

    if arr[i] in dict :
        dict[arr[i]] += 1
    else :
        dict[arr[i]] = 1
    
# O(n^2)
for j in range(m):

    s = dict.get(arr2[j])
    
    if s :
        print(s, end=' ')
    else :
        print(0,end=' ')