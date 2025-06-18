function solution(n) {
    var answer = 0;
    
    dp = Array.from({length:n+1}, () =>0 )
    // 1
    // 2
    // 1+1+1, 2+1, 1+2 = 3
    // 1+1+1+1, 1+2+1, 1+1+2, 2+1+1, 2+2 = 5
    
    for (let i=1; i<n+1; i++) {
        if (i == 1) {dp[1] = 1}
        else if (i==2) {dp[2] = 2}
        else if (i==3) {dp[3] = 3}
        else {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        }
    }
    
    
    return dp[n];
}