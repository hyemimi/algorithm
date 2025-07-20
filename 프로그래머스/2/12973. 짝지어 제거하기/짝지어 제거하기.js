function solution(s)
{
    var answer = 1;

    /**
        1. 처음에 값을 스택에 넣는다.
        2. 스택에 있는 값과 비교하여 넣으려는 값이 같다면 값을 넣지 않고 스택 pop, 다르다면 스택에 그대로 push
        3. 최종적으로 스택이 비어 있을 경우 1을 반환
    */
    
    const stack = [s[0]]
    
    for (let i=1; i<s.length; i++) {
        if (s[i] === stack[stack.length-1]) {
            // top과 문자열 비교
            stack.pop()
        }
        else {
            stack.push(s[i])
        }
    }
    
    if (stack.length > 0) {
        answer = 0
    }

    return answer;
}