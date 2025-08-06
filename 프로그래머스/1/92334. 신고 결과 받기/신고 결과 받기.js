function solution(id_list, report, k) {
    var answer = [];
    const n = id_list.length;
    const obj1 = {};
    const obj2 = {};
    
    
    // 신고 당한 애 기록 (중복 처리)
    for (let i=0; i<report.length; i++) {
        const [user, reportedUser] = report[i].split(" ")
        
        if (reportedUser in obj1) {
            obj1[reportedUser].add(user)
        }
        else {
            obj1[reportedUser] = new Set([user]);
        }
    }
    

    // obj1 돌면서 메일 처리할 것인지 확인
    for (const key in obj1) {
 
        if (obj1[key].size >= k) {
          
            // 신고 처리
            const users = obj1[key];
          
            for (const user of users) {
                if (user in obj2) {
                    obj2[user] += 1;
                }
                else {
                    obj2[user] = 1;
                }
            }
        }
    }
    
    for (const name of id_list) {
        if (name in obj2) {
            answer.push(obj2[name])
        }
        else {
            answer.push(0)
        }
    }
    
   
    
    // object 두 개 두기
    // 신고 당한 애 : key, 신고 한 애 : 집합 형태로 value
    // 유저 : key, 메일 받을 횟수
    
    
    
    
    
    return answer;
}