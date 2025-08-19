function solution(n, costs) {

    /** Solution
        최소 비용으로 모든 섬이 통행 가능하게 만들기 => 싸이클 x
        루트 노드가 같으면 싸이클
    */
    
    // 루트 노드 찾기
    function find(parent, x) {
        if (parent[x] === x) {
            // 부모 노드가 자신 => 루트 노드
            return x
        }
        
        parent[x] = find(parent,parent[x]) // 최소 신장 비용 트리 구성
        
        return parent[x]
    }
    
    // 집합을 합치는 연산
    function union(parent, rank, x, y) {
        
        const rootX = find(parent,x)
        const rootY = find(parent,y)
        
        // 큰 랭크에 작은 랭크의 루트 union
        if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        }
        else if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        }
        else {
            // 랭크가 같은 경우
            parent[rootX] = rootY;
            rank[rootY] += 1;
        }

    }
    
    
    
    costs.sort((a,b) => a[2] - b[2]); // 비용 오름차순 정렬
    
    const parent = Array.from({length:n+1}, (_, i) => i )
    const rank = Array.from({length: n+1}, () => 0)
    
    let minCost = 0;
    let edges = 0;
    
    for (const edge of costs) {
        
        if (edges === n-1) {
            break;
        }
        
        const x = find(parent, edge[0]);
        const y = find(parent, edge[1]);
        
        if (x !== y) {
            // 두 루트 노드가 다름 -> 다른 집합에 속함
            
            union(parent,rank,x,y);
            minCost += edge[2];
            edges += 1;
        }
    }
    
    
    
    return minCost;
}