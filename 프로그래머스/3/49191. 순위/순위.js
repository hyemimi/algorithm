function solution(n, results) {
    var answer = 0;
    
    const graph = Array.from({length: n+1}, () => Array(n+1).fill(0))
    
    // 노드 간 관계 초기화 - 1은 이김, -1은 짐, 0은 관계 모름
    const l = results.length
    for (let i=0; i<l; i++) {
        const [winner, loser] = results[i]
        graph[winner][loser] = 1
        graph[loser][winner] = -1
    }
  
    // 플로이드 워셜 - 노드 끼리의 관계 구하기
    for (let k=1; k<=n; k++) {
        for (let i=1; i<=n; i++) {
            for (let j=1; j<=n; j++) {
                if (graph[i][k] === 1 && graph[k][j] === 1) {
                    graph[i][j] = 1
                    graph[j][i] = -1
                }
                
            }
        }
    }

    answer = n
    
    // 순위를 정확하게 알 수 있는 선수 찾기
    for (let i=1; i<=n; i++) {
 
        for (let j=1; j<=n; j++) {
            
            if (i===j) continue
            
            // 자신을 제외한 다른 선수와의 승부를 알 수 없음
            if (graph[i][j] === 0) {
                answer -= 1
                break
            }
        }

    }
    
    
    
    return answer;
}