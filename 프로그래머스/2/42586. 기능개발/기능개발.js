function solution(progresses, speeds) {
    var answer = [];
    
    /** solution
        1. 첫 째날 - progresses 배열을 돌면서 speeds 만큼 더한다.
        2. 첫 번째 shift 대상 검사해서 100이면 pop(), 그렇지 않으면 1 반복
        3, 첫 번째 대상 shift 할 수 있게 되면 shift 하고 그 이후의 것들도 검사.
    */

    while (progresses.length > 0) {
        
        const current = progresses.shift();
        const speed = speeds.shift();
        
        if (current >= 100) {
            answer[answer.length - 1] += 1;
            continue;
        }
        const days = Math.ceil((100 - current) / speed); // 작업 일수
        answer.push(1)
        
        for (let i=0;i<progresses.length;i++) {
            progresses[i] += (speeds[i] * days)
        }

        
    }
    
    return answer;
}