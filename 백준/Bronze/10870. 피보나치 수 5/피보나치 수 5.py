n = int(input())

def fibonacchi (n):

    if n == 0 or n == 1:
        return n
    return fibonacchi(n-1) + fibonacchi(n-2)

print(fibonacchi(n))