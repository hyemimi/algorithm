
import math

a, b = map(int, input().split())
print("1" * math.gcd(a, b))  # 최대공약수의 개수만큼 '1'을 출력