# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, d = map(int, input().split())
p = list(map(int, input().split()))

# 개미 사이의 가장 긴 거리가 d 이하가 되도록 개미를 제거
# 개미는 최소로 제거함.

p.sort()

left = 0
max_count = 0

for right in range(n):

	while p[right] - p[left] > d:
		# 개미 제거
		left += 1

	max_count = max(max_count, right - left + 1)

print(n-max_count)
	
		
		

	
	
	
