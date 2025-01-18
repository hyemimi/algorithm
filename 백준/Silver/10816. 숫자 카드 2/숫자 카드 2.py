n = int(input())
arr = list(map(int,input().split()))# O(n)
m = int(input())
arr2 = list(map(int,input().split())) # O(m)

dict = {}

# O(n)
for i in range(n):
    
    #O(1)
    if arr[i] in dict :
        dict[arr[i]] += 1
    else :
        dict[arr[i]] = 1
    
# O(m)
for j in range(m):

    s = dict.get(arr2[j]) # O(1)
    
    if s :
        print(s, end=' ')
    else :
        print(0,end=' ')