function solution(N, road, K) {
    var answer = 0;

    // 1번에서 k시간 이하로 배달 가능한 마을 -> 다익스트라
    
    // 그래프 초기화
    const graph = Array.from({length : N+1}, () => Array(N+1).fill(Infinity))
    for (const [x,y,time] of road) {
        graph[x][y] = Math.min(time,graph[x][y])
        graph[y][x] = Math.min(time,graph[y][x])

    }
    
    const dist = Array(N+1).fill(Infinity) // 최단거리 배열
    const visit = Array(N+1).fill(0) // 방문 배열
   
    dist[1] = 0
    
    // N개의 마을을 돌면서 확정
    for (let i=1; i<= N; i++) {
        let current = -1
        let minDist = Infinity
        
        // 현재 방문하지 않은 노드 중에서 최단거리가 가장 작은 노드 찾기
        for (let k=1; k<=N; k++) {
            if (visit[k] !== 1 && dist[k] < minDist) {
                current = k
                minDist = dist[k]
            }
        }
        
        // 다 방문함
        if (current === -1) {
            break
        }
        
        visit[current] = 1
        
        // 노드와 연결된 모드 노드 거리 갱신
        for (let next=1; next<=N; next++) {
            
            if (visit[next] === 1) continue
            if (graph[current][next] === Infinity) continue // 연결 X
            
            const nextDist = dist[current] + graph[current][next] 
            
            // 갱신
            if (nextDist < dist[next]) {
                dist[next] = nextDist
            }
     
        }
        
        
    }
    
    for (const item of dist) {
        if (item <= K) {
            answer += 1
        } 
    }
    

    return answer;
}