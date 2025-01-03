function solution(maps) {
    var answer = 0;
    const n = maps.length;
    const m = maps[0].length;
    
    // 최단 거리 문제, BFS
    let ch = Array.from(Array(n) , ()=>Array(m).fill(0)) // 체크 배열
    let queue=[];
    
    // 동서남북 방향
    const dx = [0,0,1,-1];
    const dy = [1,-1,0,0];
  
    queue.push([0,0,1]);
    ch[0][0] = 1;
    
    while (queue.length > 0) {
        
        const [sx,sy,ans] = queue.shift();
        
        if (sx == n-1 && sy == m-1) {
            // 도착 가능
            return ans;
        } 
        
        for (let i=0 ; i < 4; i++) {
            let x = dx[i] + sx;
            let y = dy[i] + sy;
            
            if (x >= 0 && y >= 0 && x < n && y < m && maps[x][y] == 1 && ch[x][y] == 0){
                // 이동 가능
                ch[x][y] = 1;
                queue.push([x,y,ans+1]);
            }
        }
        
    }
     return -1;
    
}