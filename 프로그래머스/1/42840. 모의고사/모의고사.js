function solution(answers) {
    var answer = []
    const pattern = [
        [1,2,3,4,5], // 1번 수포자
        [2,1,2,3,2,4,2,5], // 2번 수포자
        [3,3,1,1,2,2,4,4,5,5] // 3번 수포자
    ]
    
    const scores = [0,0,0]
    
    for (const [i,answer] of answers.entries()) {
        
        for (let j=0; j<3; j++) {
               if (answer === pattern[j][i%(pattern[j].length)]) {
                    scores[j] += 1
               }
        }
    
    }
    
    let maxScore = Math.max(...scores)
    
    for (let [i,score] of scores.entries()) {
        if (score == maxScore) {
            answer.push(i+1)
        }
    }
    
    return answer;
}