def solution(info, n, m):
    answer = 0
    length = len(info)
    INF = int(1e9)
    
    dp = [INF] * m # dp[i]는 b의 흔적이 i일 때 a 흔적의 최소
    dp[0] = 0
    
    for item in info:
        # 각 물건마다 dp를 다시 계산함
        next_dp = [INF] * m 
        
        # 가능한 b의 흔적만큼 a 흔적의 최솟값을 계산함
        for i in range(m):
            
            if dp[i] == INF:
                continue
            
            # A가 훔침
            if item[0]+dp[i] < n:
                next_dp[i] = min(next_dp[i], item[0] + dp[i])
            
            # B가 훔침
            if i + item[1] < m:
                next_dp[i+item[1]] = min(next_dp[i+item[1]], dp[i])
        
        dp = next_dp
    
    answer = min(dp)
    
    return answer if answer != INF else -1