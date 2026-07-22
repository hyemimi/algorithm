function solution(n, s, a, b, fares) {
    var answer = Infinity;
    
    // 1. 다익스트라: 시작-환승지점 +환승지점-a + 환승지점-b 근데 그러면 다익스트라 두 번만 하면 되나?
    // 2. 플로이드 워셜: 전체 노드 간 최단 거리를 구하는 것이므로 O(n^3)이고, ... 어케 풀지?
    
    // fares 그래프로 변환
    const graph = Array.from({length:n+1}, () => Array(n+1).fill(Infinity))
    
    for (const [x,y,dist] of fares) {
        graph[x][y] = Math.min(dist,graph[x][y])
        graph[y][x] = Math.min(dist, graph[y][x])
    }
    
    function dijkstra(node) {
        
        const dist = Array(n+1).fill(Infinity)
        const visit = Array(n+1).fill(0)
        dist[node] = 0

        
        for (let i=1; i<=n; i++) {
               
            let current = -1
            let minDist = Infinity
            
            for (let j=1; j<=n; j++) {
                
                if (visit[j] !== 1 && dist[j] < minDist) {
                    minDist = dist[j]
                    current = j
                }
                
            }
          
        
        if (current === -1) break
        
        visit[current] = 1
        
         for (let next=1; next<=n; next++) {
            
             if (visit[next] === 1) continue
             if (graph[current][next] === Infinity) continue
             
             nextDist = dist[current] + graph[current][next]
             
             if (nextDist < dist[next]) {
                 dist[next] = nextDist
             }
             
         }
        }

        return dist 
    }
    const distS = dijkstra(s)
    const distA = dijkstra(a)
    const distB = dijkstra(b)
    
    
    // 합승 지점 k
    for (let k=1; k <= n; k++) {
        answer = Math.min(answer, distS[k] + distA[k] + distB[k])
    }
    
    
    
    return answer;
}