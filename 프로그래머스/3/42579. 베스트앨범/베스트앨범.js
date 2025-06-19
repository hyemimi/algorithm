function solution(genres, plays) {
    var answer = [];
    
    // 많이 재생된 장르 먼저
    // 장르 내에서 많이 재생된 노래 먼저
    // 재생 횟수 같으면 고유번호 낮은 노래 먼저
    
    let map = {}
    
    // 해시 기록
    for (let i=0; i<genres.length; i++) {
        if (map[genres[i]]) {
            map[genres[i]].push([plays[i],i])
        }
        else {
            map[genres[i]] = [[plays[i],i]]
        }
    }
    console.log(map)
    
    // 1. 가장 많이 재생된 장르 구하기
    let turn = []
    for (let key in map) {
        let temp = 0;
        for (let a of map[key]) {
            temp += a[0]
        }
         turn.push([temp,key]);
    }
   
    
    turn.sort((a,b) => b[0]-a[0])
    
    for (let genre of turn) {
        map[genre[1]].sort((a,b) => b[0]-a[0])
        let cnt = 0
        for (let play of map[genre[1]]) {
            cnt += 1
            if (cnt == 3) {
                break
            }
            answer.push(play[1])
        }
    }
    
    
    
    return answer;
}