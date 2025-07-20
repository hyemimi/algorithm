function solution(dirs) {
    var answer = 0;
    
    // 경계값 검사
    function isValid(x,y) {
        return -5 <= x  && x <= 5 && -5 <= y && y <= 5
    }
    
    // 명령어 변환
    function move(command,x,y) {
        switch (command) {
            case 'U':
                return [x,y+1]
            case 'D':
                return [x,y-1]
            case 'R':
                return [x+1,y]
            case 'L':
                return [x-1,y]
        }
    }
    
    const visited = new Set();
    let targetX = 0
    let targetY = 0
    
    for (ele of dirs) {
        const [nx, ny] = move(ele,targetX,targetY)
        
   

        if (isValid(nx,ny)) 
            {
                     const path1 = `${targetX},${targetY}->${nx},${ny}`;
        const path2 = `${nx},${ny}->${targetX},${targetY}`;
                
                if (!visited.has(path1) && !visited.has(path2)) {
                    
            visited.add(path1);
            visited.add(path2);
            answer++;
            
                }
                      targetX = nx
        targetY = ny
            }
       
            
            
                
  
    
    }
    
    
    
    return answer;
}