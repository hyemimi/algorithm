function solution(N, stages) {
    var answer = [];
    
    /**
        실패율 : 스테이지에 도달 했으나 클리어x 플레이어 수 / 스테이지에 도달한 플레이어 수
        stages : 사용자가 멈춰 있는 스테이지의 번호 담긴 배열
        실패율이 높은 스테이지부터 내림차순, 스테이지 번호 담은 배열 return
        
        N+1은 다 통과한 경우.
        
        1. stages에서 제일 큰 숫자를 기준으로 반복한다.
        2. 작은 스테이지부터 검색한다. (ex. 실패율 = 1의 갯수 / stages.length)
        3. 남은 사용자 수 = stages.length - 1의 갯수 
        4. 2~4을 마지막 스테이지까지 반복. 
    */
    
    const user = new Array(N+2).fill(0) // 스테이지별 도전자 수를 저장하기 위한 배열
    
    // 1. 스테이지별 도전자 수 기록
    for (let ele of stages) {
        user[ele] += 1
    }
    
    // 2. 실패율 저장 -> 해쉬 -> 스테이지 번호와 실패율 값(정렬 위함)을 같이 저장하고자
    const failure = {}
    let total = stages.length // 전체 사용자 수
    
    for (let i=1; i<=N; i++) {
        if (user[i] === 0) {
            failure[i] = 0
            continue
        }
    
        failure[i] = user[i] / total
        total -= user[i]
    }
    
    const result = Object.entries(failure).sort((a,b) => b[1] - a[1]) // 실패율로 내림차순
    return result.map((v) => Number(v[0]))
}