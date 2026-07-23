function solution(n, roads, sources, destination) {
    var answer = [];
    
    // 가중치 1로 동일, BFS 가능
    // 출발 -> 목적지까지의 최단 시간 BFS 혹은 다익스트라 가능
    // 양방향
    
    // graph 초기화
    const graph = Array.from({length: n+1}, () => [])
    const roadLength = roads.length
    
    for (let i=0; i<roadLength; i++) {
        const [a,b] = roads[i]
        graph[a].push(b)
        graph[b].push(a)
    }

    function BFS(start) {
      const visit = Array(n+1).fill(0)
      const queue = [[start,0]]
      visit[start] = 1
        
      let head = 0;
      
      while (head < queue.length) {
          const [node, cnt] = queue[head++]
          
          if (node === destination) {
              // 목적지 도달
              return cnt
          }
          
          for (const nextNode of graph[node]) {
              
              if (visit[nextNode] !== 1) {
                  visit[nextNode] = 1
                  queue.push([nextNode, cnt+1])
              }
          }
  
      }
      
      return -1
        
    }

    // 출발지점마다 최단시간 구하기
    for (const source of sources) {
        answer.push(BFS(source))
    }
    
    
    return answer;
}