# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import sys

# 덩어리 내에서 가장 점수가 높은 구역의 점수 출력하기
# 0: +1 / 2: -2

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x, y):
	queue = deque()
	queue.append([x,y])
	

	score = 0

	if board[x][y] == 2:
		score -= 2
	else:
		score += 1

	board[x][y] = 1

	while (queue):
		curX, curY = queue.popleft()
		
		for i in range(4):
			nx = curX + dx[i]
			ny = curY + dy[i]
	
			if 0<=nx<n and 0<=ny<m and board[nx][ny] != 1 :
	
				if board[nx][ny] == 0:
					# +1
					score += 1
				else:
					score -= 2
	
				queue.append([nx, ny])
				board[nx][ny] = 1
			
	return score

answer = 0

for i in range(n):
	for j in range(m):
		if board[i][j] != 1: