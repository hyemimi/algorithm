n,k = map(int,input().split())

def topDown(n,k) :
    global arr
    if (n==k or k==0) :
        return 1 % 10007
    else :
        if (arr[n][k] != 0):
            return arr[n][k]
        arr[n][k] = (topDown(n-1,k) + topDown(n-1,k-1)) % 10007
        return arr[n][k]
    
arr = [[0 for j in range(n+1)] for i in range(n+1)]   
print(topDown(n,k))