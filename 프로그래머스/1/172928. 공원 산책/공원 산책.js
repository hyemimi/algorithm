function solution(park, routes) {
    var answer = [];
    
    const n = park.length
    const m = park[0].length
    
    var cur = [0,0]
    
    // 1. 시작지점 찾기
    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (park[i][j] === 'S') {
            // 시작 지점
                cur = [i,j]
            }
        }
    }
    
    const dx = [-1,0,1,0]
    const dy = [0,1,0,-1]

    
    for (route of routes) {
        const [direction, count] = route.split(" ")
        let dir;
        let flag = true
        
         if (direction === 'N') {
            // 북쪽
            dir = [-1, 0]
        }
        
        else if (direction === 'S') {
            // 남쪽
            dir = [1, 0]
        }
        
        else if (direction === 'W') {
            // 서쪽
            dir = [0, -1]
        }
        
        else {
            // 동쪽
            dir = [0, 1]
        }
        
        const temp = [...cur]
        
        // 이동 중간에 장애물 만나면 이동 취소
        for (let k=1; k<=count; k++) {
             
             temp[0] += dir[0]
             temp[1] += dir[1]
             
             if (0 > temp[0] || temp[0] >= n || 0 > temp[1] || temp[1] >= m || park[temp[0]][temp[1]] === 'X'){
                flag = false  
                break
            }

        }
        
        if (flag === true) {
            cur = temp
        }

 
    }
    
    
    
    
    return cur;
}