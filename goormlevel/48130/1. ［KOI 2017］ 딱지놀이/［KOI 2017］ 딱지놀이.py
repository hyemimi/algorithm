# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 딱지 규칙
## 별 > 동그라미 > 네모 > 세모 / 4, 3, 2, 1

n = int(input())

def whoIsWinner(a, b):
	# a가 이길 경우 'a', 질 경우 'b'를 return 합니다.
	# 무승부일 경우, 'ab'를 return 합니다.
	
	## 별 > 동그라미 > 네모 > 세모 / 4, 3, 2, 1
	a_star = a.get(4, 0)
	b_star = b.get(4, 0)

	a_cir = a.get(3, 0)
	b_cir = b.get(3, 0)

	a_rec = a.get(2,0)
	b_rec = b.get(2,0)

	a_tri = a.get(1,0)
	b_tri = b.get(1,0)
	

	# 1. 별 갯수 비교
	if a_star > b_star:
		return 'A'
	elif a_star < b_star:
		return 'B'
	
	# 2. 동그라미 갯수 비교
	if a_cir > b_cir:
		return 'A'
	elif a_cir < b_cir:
		return 'B'

	# 3. 네모 갯수 비교
	if a_rec > b_rec:
		return 'A'
	elif a_rec < b_rec:
		return 'B'

	# 4. 세모 갯수 비교
	if a_tri > b_tri:
		return 'A'
	elif a_tri < b_tri:
		return 'B'

	return 'D' # 무승부

# 2n 개의 줄 동안 딱지 갯수 & 상태
answer = []

for i in range(n):

	# a 입력
	a_inputs = list(map(int, input().split()))
	a_num = a_inputs[0]
	a_status = a_inputs[1:]

	# b 입력
	b_inputs = list(map(int, input().split()))
	b_num = b_inputs[0]
	b_status = b_inputs[1:]

	# 각각 해시화
	a_dict = {}
	b_dict = {}
	for j in range(a_num):
		pattern = a_status[j]
		a_dict[pattern] = a_dict.get(pattern, 0) + 1

	for j in range(b_num):
		pattern = b_status[j]
		b_dict[pattern] = b_dict.get(pattern, 0) + 1

	answer.append(whoIsWinner(a_dict, b_dict))

for ans in answer:
	print(ans)

		


