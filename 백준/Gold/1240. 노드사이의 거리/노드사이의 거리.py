from collections import deque

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    n1,n2,dis = map(int,input().split())

    graph[n1].append((n2,dis)) # 연결된 노드, 간선
    graph[n2].append((n1,dis))


# 1 -> 2 까지의 거리는 계속 타고 타고 가는 것. 간선 더하면서. dfs도 되고 bfs도 된다


for k in range(m):
    n1, n2 = map(int,input().split())
    queue = deque()
    queue.append((n1,0))
    visited = [0] * (n+1)
    visited[n1] = 1
    cnt = 0

    while (len(queue) > 0):
        node, dis = queue.popleft();

        if node == n2 :
            # 도달
            print(dis)
            break

        for (next,nextDis) in graph[node]:
            if (visited[next] != 1):
                # 방문하지 않은 경우 방문
                queue.append((next, dis + nextDis))
                visited[next] = 1
