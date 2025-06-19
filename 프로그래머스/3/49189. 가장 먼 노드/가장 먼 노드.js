function solution(n, edge) {
    var answer = 0;
    
    const graph = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edge) {
        graph[a].push(b);
        graph[b].push(a); // 양방향 그래프
    }

    // DFS로, 최장 경로 구하기 ?
   
    queue = [[1,0]]
    let ch = Array.from({length: n+1}, () => 0);
    ch[1] = 1
    let cnt = 0;

    while (queue.length > 0) {
        [current,dist] = queue.shift();

        // 인접한 노드 탐색
        for (next of graph[current]) {
            
            if (ch[next] === 0) {
                queue.push([next,dist + 1])
                ch[next] = dist + 1
            }
 
        }
    }

    
    maxDistance = Math.max(...ch)
    for (let ele of ch) {
        if (maxDistance == ele) {
            answer += 1
        }
    }
    
   
    
    return answer;
}