function solution(begin, target, words) {
    var answer = 0;
    
    /**
    BFS (최소 몇 단계)
    */
    let queue = [];
    queue.push([begin,0,-1]); //  word(현재 word), step (전환 단계), shift된 index
    
    while (queue.length > 0) {
        let [shiftWord, shiftStep,shiftIdx] = queue.shift();

        if (shiftWord == target) {
        // 종료
            answer = shiftStep;
            break;
        }
        if (shiftIdx  == words.length - 1) {
            // 바꿀 수 없음 (전부 검사함)
            answer = 0;
            break;
        }

        for (let i=0; i<words.length; i++) {
            // words 배열과 검사해서 한글자만 다르면 queue에 push
            let count = 0;
            for (let j=0; j<words[i].length;j++){
                // 한 단어만 같은지 확인
                let temp = words[i];
                if (temp[j] == shiftWord[j]) count++;
            }
            if (count == words[i].length - 1) {
                queue.push([words[i],shiftStep+1,i]);
            };
            
        }
    }
    
    return answer;
    
}