function solution(maps) {
    let answer = -1;
    
    // 레버를 먼저 당기고 출구로 이동
    // 최소 시간
    // 방문 여부 + 레버 여부 같이 체크
    
    const n = maps.length
    const m = maps[0].length
    
    const visited = Array.from({length: n+1}, () => Array.from({length:m+1}, () => Array(2).fill(0)))

    const dx = [-1,1,0,0]
    const dy = [0,0,1,-1]
    
    const queue = []
    
    // maps 순회 -> 시작지점, 레버지점, 출구 확인
    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (maps[i][j] === 'S') {
                queue.push([i,j,0,0])
            }
        }
    }

    let head = 0;
    
    while (head < queue.length) {
        const [x, y, k, time] = queue[head++] // 좌표 x, y, 레버 여부, 최단시간
        
        if (maps[x][y] === 'E' && k === 1) {
            return time
        }
        
        for (const idx of [0,1,2,3]) {
            const nx = x + dx[idx]
            const ny = y + dy[idx]
            
            if (0<= nx && nx < n && 0<= ny && ny < m && visited[nx][ny][k] === 0 && maps[nx][ny] !== 'X') {
                
                
                if (maps[nx][ny] === 'L') {
                    visited[nx][ny][1] = 1
                    queue.push([nx,ny,1,time + 1])
                    continue
                }
                
                if (maps[nx][ny] !== 'X') {
                    visited[nx][ny][k] = 1
                    queue.push([nx,ny,k,time + 1])
                }

            }
            
        }
    }
    
    
    
    return answer;
    
}