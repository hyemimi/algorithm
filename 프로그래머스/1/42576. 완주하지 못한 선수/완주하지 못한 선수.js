function solution(participant, completion) {
    var answer = '';
    
    const people = {};
    
    // 해시 저장
    for (const person of participant) {
        if(people[person]) {
            people[person] += 1;
        }
        else {
            people[person] = 1;
        }
    }
    
    // 완료한 사람 -1
    for (const completePerson of completion) {
        people[completePerson] -= 1;
    }
    
    for (const key in people) {
        if (people[key] > 0) {
            return key;
        }
    }
    
    
    
    return answer;
}