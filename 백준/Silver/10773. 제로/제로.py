arr = []
k = int(input())


for i in range(k):
    n = int(input())

    

    if n != 0 :
        arr.append(n)
    else :
        arr.pop(-1)


print(sum(arr))