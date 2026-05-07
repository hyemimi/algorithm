import heapq
import sys

def solution(n, s, a, b, fares):
    INF = sys.maxsize
    answer = INF
    
    # s에서 출발해서 a, b로 택시를 탐
    # 합승을 하지 않아도 됨.
    # 둘이 겹치는 지점에서 하차, 각각 택시를 타서 계산함.
    # 돌아가지 않는 게 좋음. 사이클 x
    
    graph = [[] for _ in range(n+1)]
    
    # 그래프 초기화
    for fare in fares:
        node1,node2,cost = fare[0],fare[1],fare[2]
        graph[node1].append((node2,cost))
        graph[node2].append((node1,cost))
        
    
    # 다익스트라
    def dijkstra(start):
        pq = []
        dist = [INF] * (n+1)
        heapq.heappush(pq,(0,start))
        dist[start] = 0
        
        while(pq):
            cost, node = heapq.heappop(pq)
            
            for node in graph[node]:
                nextNode = node[0]
                nextCost = cost + node[1]
                
                if (nextCost > dist[node[0]]):
                    # 이미 최소임
                    continue
                
                dist[nextNode] = nextCost
                heapq.heappush(pq, (nextCost, nextNode))
        
        return dist
    
    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    
        
    for k in range(1,n+1):
        # 중간 지점 k

        answer = min(answer, dist_s[k] + dist_a[k] + dist_b[k])
        
    
    return answer