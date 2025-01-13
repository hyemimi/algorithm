import heapq


# 문제: x에서 출발해서 *최단 거리*가 k가 되는 정점 출력 
# 도시의 갯수 n, 도로 갯수 m, 최단거리 k, 시작 노드 x
n,m,k,x = map(int,input().split())
graph= [[] for _ in range(n+1)]

INF = int(1e9)
dist = [INF] * (n+1) # 거리 저장 


# 그래프 입력 (인접리스트)
for i in range(1,m+1):
    v1,v2 = map(int,input().split())

    graph[v1].append(v2)



pq = []
heapq.heappush(pq,(0,x))
dist[x] = 0


while (pq):
    edge, node = heapq.heappop(pq)
    
    # 이미 갱신됨 
    if dist[node] < edge :
        continue

    for i in graph[node]:

        cost = edge + 1

        # 갱신
        if cost < dist[i]:
            dist[i] = cost
            heapq.heappush(pq,(cost,i))

isFind = False

for i in range(1,n+1):
    if dist[i] == k :
        isFind = True
        print(i)


if isFind == False : print(-1)

