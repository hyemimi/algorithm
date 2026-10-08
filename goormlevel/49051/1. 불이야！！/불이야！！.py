# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from collections import deque

# @ : 불이 난 위치 / &: 현재 위치 / #: 벽 / . : 빈칸

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
queue = deque()

# 불이 난 위치, 시작 위치 확인
for i in range(r):
	for j in range(c):
		if board[i][j] == '@':
			fire = (i,j)
			queue.append((i,j,0))
			board[i][j] = '#'
		elif board[i][j] == '&':
			end = (i,j)
		


dx = [-1,1,0,0]
dy = [0,0,-1,1]

# visit = [[0] * (c) for _ in range(r)]
# visit[fire[0]]visit[fire[1]] = 1


canFireGo = False

while (queue):
	x, y, time = queue.popleft()

	if (x,y) == end:
		# 구름이의 자리까지 번짐
		print(time - 1)
		canFireGo = True
		break

	for i in range(4):
		nx = dx[i] + x
		ny = dy[i] + y

		if 0<=nx<r and 0<=ny<c and board[nx][ny] != '#':
			queue.append((nx,ny, time + 1))
			board[nx][ny] = '#' # 방문 처리

if canFireGo == False:
	print(-1)	

	
	





