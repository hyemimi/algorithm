n = int(input())

arr = list(map(int,input().split()))
cnt = 0


def isPrime(n):
    if n < 2: return False
    
    for i in range(2, n):
        if n % i == 0:
            return False  
        
    return True

for i in range(n):
    if isPrime(arr[i]) : cnt += 1


print(cnt)