# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, k = map(int, input().split())

# 직사각형 영역 중 겹치는 종이 k개인 영역의 총 넓이 구하기
specs = []

for i in range(n):
	specs.append(list(map(int, input().split())))


board = [[0] * 1001 for _ in range(1001)]




for spec in specs:
	x1, y1, x2, y2 = spec

	# board 칠하기
	board[x1][y1] += 1
	board[x1][y2] -= 1
	board[x2][y2] += 1
	board[x2][y1] -= 1

answer = 0

# 1. 가로 방향 누적합
for i in range(1001):
    for j in range(1, 1001):
        board[i][j] += board[i][j-1]

# 2. 세로 방향 누적합
for i in range(1, 1001):
    for j in range(1001):
        board[i][j] += board[i-1][j]

for i in range(1001):
	for j in range(1001):
		if board[i][j] == k:
			answer += 1
		
print(answer)
	

