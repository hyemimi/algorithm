import math

a, b = map(int,input().split())
c, d = map(int,input().split())

e = a*d + c * b
f = b*d

print(e//math.gcd(e,f), f//math.gcd(e,f))