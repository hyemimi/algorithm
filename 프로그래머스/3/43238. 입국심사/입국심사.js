function solution(n, times) {
    var answer = 0;
    
    // 시간을 기준으로 탐색하는 이분탐색
    // 최대 시간은 n * 1 000 000 000 (심사대가 한 개인 경우)
    let left = 1
    let right = n * 1000000000
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        
        let total = 0
        for (const time of times) {
            // 각 심사대마다 mid 시간 동안 심사할 수 있는 사람 수
            total += Math.floor(mid / time)
        }
        
        if (total >= n) {
            answer = mid
            right = mid - 1
        }
        else {
            left = mid + 1
        }
    }
    
    
    
    return answer;
}