from collections import deque



# 금으로 막혀있어 지나갈 수 없는 칸은 '#'으로 표현되고,
# 비어있는 칸은 '.'으로 표현된다. 시작 지점은 'S'로 표현되고, 
# 탈출할 수 있는 출구는 'E'로 표현

while(True):

    # l: 층수, r: 층의 행, c: 열
    l,r,c = map(int,input().split())

    # 테스트 케이스 끝
    if l==0 and r==0 and c==0 :
        break

    queue = deque()
    dx = [-1,0,1,0,0,0]
    dy= [0,1,0,-1,0,0]
    dz = [0,0,0,0,-1,1]
    check = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]

    # 빌딩 입력 
    building = []
    for i in range(l):

        temp = [list(input()) for _ in range(r+1)]
        building.append(temp)

    # 시작지점, 도착지점  
    for z in range(l):
        for x in range(r):
            for y in range (c):
                if building[z][x][y] == 'S':
                    check[z][x][y] = 1
                    start = (z,x,y,0)
                if building[z][x][y] == 'E':
                    end = (z,x,y)
    
    queue.append(start)

    isCompleted = False

    while(len(queue) > 0) :
        z,x,y,cnt = queue.popleft()

        if z == end[0] and x == end[1] and y == end[2]:
            print('Escaped in',cnt,'minute(s).')
            isCompleted = True
            break

        for i in range(6):
            nz,nx,ny,ncnt = z+dz[i], x+dx[i], y+dy[i], cnt + 1

            if 0 <= nz < l and 0 <= nx <r and 0 <= ny < c and building[nz][nx][ny] != '#' and check[nz][nx][ny] == 0:
                queue.append((nz,nx,ny,ncnt))
                check[nz][nx][ny] = 1
    
    
    if isCompleted == False : print('Trapped!')