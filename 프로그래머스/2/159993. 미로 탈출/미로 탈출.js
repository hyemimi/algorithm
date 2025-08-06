function solution(maps) {
    let answer = -1;
    const n = maps.length;
    const m = maps[0].length;
    const queue = [];
    
    // 미로 탈출 최소 시간
    // 레버를 당긴 후 출입문으로 이동해야 함
    // 따라서, 레버 당김 여부를 3차원 배열로 관리
    
    
const visited = Array.from(Array(n), () => Array(m).fill(false).map(() => Array(2).fill(false)))
let endX = -1;
let endY = -1;

    // 시작, 종료 지점 탐색
    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (maps[i][j] === 'S') {
                queue.push([i,j,0,0]) // x, y, 레버 여부, 시간
                visited[i][j][0] = true;
            }
            else if (maps[i][j] === 'E') {
                endX = i;
                endY = j;
            }
        }
    }
    
const dx = [-1,0,1,0]
const dy = [0,1,0,-1]

    while(queue.length > 0) {
        const [x, y, k, time] = queue.shift();
        
        if (x === endX && y === endY && k === 1) {
            // 도착
            answer = time;
            break;
        }
        
        for (let s=0; s<4; s++) {
            
            const nx = x + dx[s];
            const ny = y + dy[s];

            if (0<= nx &&  nx < n && 0<= ny && ny <m  && maps[nx][ny] === 'L' && visited[nx][ny][k] ===false) {
                visited[nx][ny][1] = true;
                queue.push([nx,ny,1,time + 1]);
            }
            
            if (0<= nx &&  nx < n && 0<= ny && ny <m && maps[nx][ny] !== 'X' && visited[nx][ny][k] === false) {
                // 이동 가능
                visited[nx][ny][k] = true;
                queue.push([nx,ny,k, time + 1])
                
            }
        }
        
        
    }
  

    
    return answer;
    
}