from collections import deque

t = int(input())


dx = [-2,-2,-1,1,2,2,1,-1]
dy = [1,-1,2,2,-1,1,-2,-2]


while (t>0):

    l = int(input())
    a, b = map(int,input().split())
    c, d = map(int, input().split())

    check = [[0] * (l) for _ in range(l)]
    
    queue = deque()
    queue.append((a,b,0))
    check[a][b] = 1

    while(queue):

        currentx, currenty, count = queue.popleft()


        if currentx == c and currenty == d:
            # 목적지 도달
            print(count)
            break

        for i in range(len(dx)):
            nx = currentx + dx[i]
            ny = currenty + dy[i]
            ncount = count + 1

            
            if 0 <= nx < l and 0 <= ny < l and check[nx][ny] == 0 :
                queue.append((nx,ny,ncount))
                check[nx][ny] = 1
                

    

    t -= 1