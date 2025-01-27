from collections import deque

n,m = map(int,input().split())
graph = [[]  for _ in range(n+1)]
dist = [-1] * (n+1)

# 냄새는 1번 헛간에서의 거리(여기서 거리라 함은 지나야 하는 길의 최소 개수이다)가 멀어질수록 감소한다고 한다. 
# 재서기의 발냄새를 최대한 숨길 수 있는 헛간을 찾을 수 있게 도와주자!


for i in range(m):
    a,b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)


queue = deque()
queue.append((1))
dist[1] = 0

while(len(queue) > 0):
    node = queue.popleft()

    for i in graph[node]:

        if dist[i] == -1:
            dist[i] = dist[node] + 1
            queue.append((i))



max_dist = max(dist)
num = 0
ans = []

for i in range(1,n+1):

    if dist[i] == max_dist:
        num += 1
        ans.append(i)

print(ans[0],max_dist, num) # 헛간 번호, 가장 먼 거리, 거리가 같은 헛간 갯수 