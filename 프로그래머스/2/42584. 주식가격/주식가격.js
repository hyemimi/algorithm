function solution(prices) {
    var answer= new Array(prices.length).fill(0);
  
    /** 
    1. stack 사용해서 넣기
    2. 이전 값(스택 top 값)과 비교해서 작다면 pop 하고, pop한 인덱스 길이 1 처리
    3. 이전 인덱스 값도 비교해서 떨어졌다면 pop 해서 인덱스 길이 처리
    4. 해당 인덱스도 push
    5. 끝까지 반복
    6. 스택에 남아 있는 값은 전체 길이 - 해당 인덱스 - 1
    */
    
    const stack = [0];
    
    for (let i=1; i<prices.length; i++) {

        while (stack.length > 0 && prices[i] < prices[stack[stack.length-1]]) {
           
                const idx = stack.pop();
                answer[idx] = i - idx;       
            
        }
        stack.push(i)
    }
    
    while (stack.length >0) {
        let topIdx = stack.pop();
        answer[topIdx] = prices.length - 1 - topIdx
    }
    
    return answer;
}