from collections import deque

n = int(input()) # 동기의 수
m = int(input()) # 리스트의 길이

graph = [[] for _ in range(n+1)]
check= [0] * (n+1)

for i in range(1,m+1):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def BFS(v):
    queue = deque()

    queue.append((v,0))
    check[v] = 1
    cnt = 0

    while (len(queue) > 0) :
        vertex,depth = queue.popleft()

        if depth >= 2 :
            break

        for v2 in graph[vertex]:
        # 연결 노드 확인
            if check[v2] == 0 :
                check[v2] = 1
                queue.append((v2,depth + 1))
                cnt += 1
             
       
    
    return cnt



print(BFS(1))