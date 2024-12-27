from collections import deque;

n, m = map(int,input().split())

arr = [[0] *(n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)



def BFS(v):

    queue = deque()
    queue.append((v))
    visited[v] = 1
    count = 0

    while(len(queue) > 0):
        V = queue.popleft()
        for ele in arr[V]:

            if (visited[ele] != 1):
                    queue.append((ele))
                    visited[ele] = 1
            

ans = 0

for i in range(1,n+1):
    if (visited[i] != 1):
        BFS(i)
        ans += 1
    
print(ans)

