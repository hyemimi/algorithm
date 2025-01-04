function solution(n, lost, reserve) {
    var answer = 0;
    let newArr = []
    lost = lost.sort()
    reserve = reserve.sort()
    // 빌려줄 수 없는 경우 제외
    let temp2 = 0
 
    for (let i=0;i<reserve.length;i++) {
        const a = lost.indexOf(reserve[i])
        console.log(a)
        if (a >= 0) {
            lost[a] = 0
            reserve[i] = 0
        }
    }
    
    console.log(lost,reserve)
    
     
    // 앞, 뒤 번호에게만 체육복을 빌려줄 수 있음 
    // 체육복을 도난 당했는데 여벌이 있는 경우 다른 학생에게 빌려줄 수 x
        
    for (let i=0; i<lost.length;i++) {
    
        let isOkay = false
    
        
         for (let j=0; j<reserve.length; j++) {
             
             
             if (lost[i] !== 0 && reserve[j] !== 0 && reserve[j] == lost[i] - 1) {
                 reserve[j] = 0
                 isOkay = true
                 break
             }
             else if (lost[i] !== 0 && reserve[j] !== 0 && reserve[j]  == lost[i] + 1) {
                 reserve[j] = 0
                 isOkay = true
                 break
             }
        }
        
        if (isOkay === true) {
            answer += 1
            lost[i] = 0
        } // 빌림 성공한 횟수 
        
        
    }
 
    
    let temp = 0
    for (let k=0; k<lost.length; k++) {
        if (lost[k] !== 0) temp += 1
    }
    
    answer = n - temp

    return answer;
}