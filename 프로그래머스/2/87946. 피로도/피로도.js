
function solution(k, dungeons) {
    var answer = 0;
    
    // 현재 피로도 k
    // dungeons는 각각 최소 필요도, 소모 필요도 배열
    // 가장 많이 돌 수 있는 던전의 갯수
        
    const n = dungeons.length;
    
    function DFS(k, cnt, visited) {
        // 방문한 적 있으면 RETURN
        // 방문한 적 없고, 현재 피로도에 맞게 방문할 수 있다면 방문
        // 방문 순서 모두 고려해야 함.
        answer = Math.max(answer, cnt);
        
        for (let i=0; i<n; i++) {
            if (visited[i] === 1) continue; // 방문한 적 있는 경우 방문할 수 없음
            if (k < dungeons[i][0]) continue; // 최소 체력 만족 못하면 방문할 수 없음

            visited[i] = 1;
            DFS(k-dungeons[i][1], cnt + 1, visited);
            visited[i] = 0;
            
            
         }

    }
    const visited = Array.from({length:n}, ()=>0);

    DFS(k, 0, visited);
    
    return answer;
}