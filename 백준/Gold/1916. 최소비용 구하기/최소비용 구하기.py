import heapq

n = int(input())
m = int(input())



INF = int(1e9)

graph =[[INF] * (n+1) for _ in range(n+1)]


for i in range(1,n+1):
    # 본인 0
    graph[i][i] = INF

# 비용 정보 입력
for i in range(m):

    s,e,p = map(int,input().split())

    if ( p > graph[s][e] ):
        #이미 간선이 존재
        continue

    graph[s][e] = p


start,end = map(int,input().split())


# 다익스트라: 방문하지 않은 노드 중에서, 가장 거리가 짧은 것 선택 후 갱신 성공하면 pq에 넣음.
# 이미 방문했었던 노드를 지나가는 로직 필요
def dikstra (graph,start,end):

    pq = []
    distance = [INF] * (n+1) # 최단 거리 기록 테이블
    distance[start] = 0  # 시작 지점으로 가는 비용은 0
    heapq.heappush(pq,(0,start)) 
    
    while(pq):
        dist, now = heapq.heappop(pq) # 현재 최단거리 테이블에서 비용이 가장 적은 것

        if (distance[now] < dist):
            # 이미 방문함
            continue

        for i in range(1,n+1):
            cost = dist + graph[now][i]

            if (cost < distance[i]):
                # 갱신
                distance[i] = cost
                heapq.heappush(pq,(distance[i], i))
    
    return distance[end]

print(dikstra(graph,start,end))

