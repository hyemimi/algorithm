function solution(n, computers) {
    // 연결 갯수 구하기
    let answer = 0;
    
    ch = Array.from({length:n+1}, () => 0);
    
    
    function DFS(v){
        ch[v] = 1
        
        for (let i=0;i<n;i++) {
            if (i===v) continue;
            if (ch[i] != 1 && computers[v][i] == 1) {
                // 방문한 적 없고, 연결 되어 있다면
                DFS(i)
            }
        }
    }
    
    for (let i=0;i<n;i++) {
        if (ch[i] != 1) {
            // 방문한 적이 없다면
            DFS(i)
            answer += 1
        }
        
    }
    
    return answer;
}
