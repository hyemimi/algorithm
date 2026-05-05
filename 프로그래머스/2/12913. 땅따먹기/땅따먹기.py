def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    # DP
    # 연속 열은 밟을 수 없음.
    # dp[i][j] = 땅따먹기 board[i][j] 위치의 얻을 수 있는 점수의 최댓값
    
    dp = [[0] * (m) for _ in range(n)]
    
    # 첫 번째 행 초기화
    for j in range(m):
        dp[0][j] = land[0][j]
    
    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                if j != k:
                    dp[i][j] = max(dp[i-1][k] + land[i][j], dp[i][j])
            

    return max(dp[n-1])