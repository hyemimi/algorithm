function solution(info, edges) {
    var answer = 0;
    const n = info.length;
    
    /** Solution
        양 <= 늑대이면 잡아먹힘
        edges 배열은 단순 연결된 간선리스트 -> 트리 구성 필요
        현재까지 방문 가능한 모든 노드 집합을 관리해야 함.
        다시 올라가서 다른 곳 방문할 수 있음 (백트래킹)
        여기서는 방문했던 노드의 자식 노드를 모두 가능한 노드에 넣어 두어 언제든 방문할 수 있게 함 
    **/
    
    // edges 배열 -> 트리 구성
    const tree = Array.from({length : n+1}, () => []);
    
    for (const [parent, child] of edges) {
        tree[parent].push(child)
    }
    
    let maxSheep = 0;
    
    function DFS (curSheep, curWolf, possible) {
        
        maxSheep = Math.max(curSheep, maxSheep);
        
        for (let i=0; i<possible.length; i++) {
            const next = possible[i];
            const nextPossible = [...possible]
            nextPossible.splice(i,1); // 방문 처리 하여 방문 가능한 노드에서 제거
            nextPossible.push(...tree[next]); // 방문하는 노드의 자식 노드 추가
            
            if (info[next]) {
                // 늑대
                if (curSheep > curWolf + 1) {
                    // 방문 가능
                    DFS(curSheep, curWolf + 1, nextPossible);
                }
            }
            else {
                // 양
                DFS(curSheep + 1, curWolf ,nextPossible);
            }
        }
        
    }
    
    DFS(1,0,tree[0])
    
   
    
    
    return maxSheep;
}