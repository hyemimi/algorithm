n = int(input())

d = 2

while (d <= n):
    if n % d == 0:
        # 나누어 떨어짐
        n = n / d
        print(d)
    else :
        d += 1