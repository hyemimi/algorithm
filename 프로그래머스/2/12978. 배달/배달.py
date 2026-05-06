import heapq

def solution(N, road, K):
    answer = 0

    # k 시간 이하로 배달할 수 있는 곳의 갯수 return
    # 1번에서 시작 -> 최단 경로 문제
    # road 에서 [마을1, 마을2, 시간]
    # 가중치 있음 -> 다익스트라. 없으면 BFS
    
    INF = int(1e9)
    dist = [INF] * (N+1) # 최단거리 저장용
    dist[1] = 0
    pq = []
    heapq.heappush(pq, (1, 0)) # 현재 노드, 현재 시간
    graph = [[] for _ in range(N+1)]
    
    for node in road:
        a = node[0]
        b = node[1]
        cost = node[2]
        
        graph[a].append((b,cost))
        graph[b].append((a,cost))
        
    
    while pq:
        node, time = heapq.heappop(pq)
        
        for info in graph[node]:
            nextNode, cost = info
            
            if dist[nextNode] < time + cost:
                # 이미 작음
                continue
            
            dist[nextNode] = cost + time
            heapq.heappush(pq, (nextNode, time + cost))
            
    print(dist)
        
    for item in dist:
        if item <= K:
            answer += 1
    
    
    return answer