def calculate(p,q) :

    if p % q == 0:
        return True
    
    return False


n, k = map(int,input().split())

arr=[]


for i in range(1,n+1):

    if (calculate(n,i)) :
        arr.append(i)

arr.sort()

if (len(arr) < k) : print(0)
else :

    print(arr[k-1])
