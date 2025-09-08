function solution(n, info) {
    let answer = Array(11).fill(0);
    let maxDiff = -1;
    
    function isBetter(a, b) {
        for (let i = 10; i >= 0; i--) {
            if (a[i] > b[i]) return true;
            else if (a[i] < b[i]) return false;
        }
        return false;
    }

    function DFS(usedShot, appeachScore, ryanScore, count, currentRyan) {
    
        // 1. 주어진 화살 다 쓴 경우 (백트래킹)
        if (usedShot > n) return;

        // 2. 라이언의 양궁 점수 다 채운 경우
        if (count > 10) {
            // 점수 계산
            if (usedShot < n) currentRyan[10] += (n - usedShot);
            let diff = ryanScore - appeachScore;
            
            if (diff > maxDiff || (diff === maxDiff && isBetter(currentRyan, answer))) {
                maxDiff = diff;
                answer = [...currentRyan];
            }
           
            return;
        }
        
        // 3. 라이언이 점수 얻는 경우
        if (n > usedShot) {
            let newRyan = [...currentRyan];
            newRyan[count] = info[count] + 1;
            DFS(usedShot + info[count] + 1, appeachScore, ryanScore + (10-count), count + 1, newRyan);
        }
        
        // 4. 어피치가 점수 얻는 경우
        if (info[count] > 0) {
             DFS(usedShot, appeachScore + (10-count), ryanScore, count + 1, currentRyan);
        }
        
        // 5. 둘 다 못 받는 경우 (0점)
        else {
            DFS(usedShot, appeachScore, ryanScore, count + 1, currentRyan);
        }
     
    }
    
    
    DFS(0,0,0,0,answer)

    
    
    return maxDiff <= 0 ? [-1] : answer;
}