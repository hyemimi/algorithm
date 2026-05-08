import heapq

def solution(n, paths, gates, summits):
    
    INF = int(1e9)
    
    # 출입구는 하나만 골라서 처음과 끝에 배치
    # 휴식 없이 이동해야 하는 시간 중 가장 긴 시간 : intensity
    # intensity가 최소가 되도록.
    
    # graph 초기화
    graph = [[] for _ in range(n+1)]
    for path in paths:
        i,j,w = path[0], path[1], path[2]
        graph[i].append((w,j))
        graph[j].append((w,i))
        
    # 산봉우리 집합
    set_summits = set(summits)
    
    # 최단 경로 구하기
    
    pq = []
    min_int = [INF] * (n+1) # start 노드에서 나머지 노드까지의 최소 intensity 저장
    # 출입구 우선순위 큐에 넣기
    for gate in gates:
        heapq.heappush(pq,(0,gate)) # intensity, 노드
        min_int[gate] = 0

    # 다익스트라
    while(pq):
        intensity, node = heapq.heappop(pq)
        
        if intensity > min_int[node]:
            continue
        
        if node in set_summits:
            # 산봉우리에 도착하면 검사X
            continue

        for next in graph[node]:
            # 다음 노드로 이동
            
            nextNode = next[1]
            nextIntensity = max(intensity, next[0])
            
            if min_int[nextNode] > nextIntensity:
                # 최솟값보다 다음 노드의 intensity가 작을 경우,최솟값 갱신.
                min_int[nextNode] = nextIntensity
                heapq.heappush(pq, (min_int[nextNode], nextNode))
                
                
                
    answer = [0, INF] # 산봉우리 번호, intensity 최솟값 찾기 위한 초기화
    for summit in sorted(summits):
        if answer[1] > min_int[summit]:
            answer = [summit, min_int[summit]]
    
    
           
    
    return answer