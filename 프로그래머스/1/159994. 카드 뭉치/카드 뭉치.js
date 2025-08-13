function solution(cards1, cards2, goal) {
    var answer = 'Yes';
    
    /** solution
        cards1[0], cards2[0]로 goal의 문자를 만들 수 있는지 검사.
        만들 수 있다면 shift()
    */
    const n = goal.length;
    
    for (let i=0; i<n; i++) {
        const targetWord = goal[i];
        
        if (cards1[0] === targetWord) {
            cards1.shift()
            continue;
        }
        else if (cards2[0] === targetWord) {
            cards2.shift()
        }
        else {
            return "No";
        }
        
    }
    return answer;
}