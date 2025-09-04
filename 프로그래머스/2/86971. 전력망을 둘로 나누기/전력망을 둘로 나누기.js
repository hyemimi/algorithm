function solution(n, wires) {
    var answer = -1;
    
    const graph = Array.from({length: n+1}, () => []) // 인접리스트 형태
    
    // graph 생성
    for (const [a, b] of wires) {
        graph[a].push(b);
        graph[b].push(a);
    }
    
    // 트리 노드 세는 함수 (깊이 우선 탐색)
    function DFS(node, parent) {
        // node, parent는 전선 끊은 노드
        // 그래프 내에서 몇 개까지 연결되어 있는지 탐색
        let cnt = 1;
        
        for (const child of graph[node]) {
            if (child !== parent) {
                 cnt += DFS(child,node)
            }         
        }
        return cnt;     
    }
    
    let minDiff = Infinity; // 최소 송전탑 차이
    
    for (const [a,b] of wires) {
        graph[a].splice(graph[a].indexOf(b), 1) // a->b 간선 제거
        graph[b].splice(graph[b].indexOf(a),1) // b->a 간선 제거
        
        const aCnt = DFS(a,b);
        const bCnt = n - aCnt;
        minDiff = Math.min(minDiff, Math.abs(aCnt - bCnt));
        
        graph[a].push(b);
        graph[b].push(a);
        
    }
    
    
    return minDiff;
}