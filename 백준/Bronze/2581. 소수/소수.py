
def isPrime(a):

    if a < 2 :
        return False
    
    for i in range(2,a):
        
        if a % i == 0 :
            return False
    
    return True

a = int(input())
b = int(input())


ans = 0
minValue = int(1e9)
for i in range(a,b+1):

    if isPrime(i):
        ans += i
        minValue = min(minValue, i)


if minValue == int(1e9) : 
    print(-1)
else :
    print(ans)
    print(minValue)
