function solution(record) {
    var answer = [];
    
    /** solution
        Action : Enter, Leave, Change
        Action Id Name
        
        - 이름을 오브젝트로 관리?
        
        record 배열을 돌면서, Enter -> 오브젝트에 id : name 과 같은 형식으로 저장
        Leave -> answer 배열에 obj[uid]님이 나갔습니다. 로 기록
        
        아 근데 Enter일 때 최종 이름을 반영해야 하는데..
        1. record 배열을 먼저 돌고, Leave 일 경우를 기준으로 최종 이름을 반영해서 ..
        2. 다시 record 돌면서 Action + uid를 기준으로 result 배열 만들자!
    */
    
    function getMessage (action, name) {
        switch (action) {
            case "Enter":
                return name + "님이 들어왔습니다.";
            case "Leave":
                return name+ "님이 나갔습니다.";
        }
        
    }
    
    const n = record.length;
    const nameObj = {};
    
    for (const word of record) {
        const [action, uid, name] = word.split(" ");
        
        if (action === 'Enter' || action === 'Change') {
            nameObj[uid] = name;
        }
    }
    
    for (const word of record) {
        const [action, uid, name] = word.split(" ");
        
        if (action === 'Enter' || action === 'Leave') {
            answer.push(getMessage(action, nameObj[uid]))
        }
    }
    
    
    
    
    
    
    
    return answer;
}