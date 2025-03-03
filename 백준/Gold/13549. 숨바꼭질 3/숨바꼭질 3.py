from collections import deque

n, k = map(int,input().split())
visited = [0] * 1000001

def BFS():
    queue = deque()
    queue.append((n,0))
    visited[n] = 1
    # 순간이동(0초)하거나, X-1, X+1 이동하거나(1초)

    while( len(queue) > 0 ):
        nx, nt = queue.popleft()

        if nx == k:
            print(nt)
            return

        if 0 <= nx*2 <=100000 and visited[nx*2] == 0:
            queue.append((nx*2,nt))
            visited[nx*2] = 1

        if 0 <= nx-1 <= 100000 and visited[nx-1] == 0:
            queue.append((nx-1,nt+1))
            visited[nx-1] = 1
        
        if 0 <= nx+1 <=100000 and visited[nx+1] == 0:
            queue.append((nx+1,nt+1))
            visited[nx+1] = 1

BFS()