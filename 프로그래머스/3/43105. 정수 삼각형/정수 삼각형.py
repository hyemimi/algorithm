def solution(triangle):
    answer = 0
    n = len(triangle)
    
    # 점화식 세워보기
    # (1,0) => (2,0) (2,1)  (x+1, y) (x+1, y+1) 
    # (1,1) => (2,1) (2,2) (x+1, y) (x+1, y+1)
    # (2,1) => (3,1) (3,2) (x+1, y) (x+1, y+1)
    # 마지막 줄 제외
    # 최댓값을 return 해야함.
    
    
    for i in range(1, n):
        m = len(triangle[i])
        for j in range(m):
            
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
                continue
            if j == m-1:
                triangle[i][j] += triangle[i-1][j-1]
                continue
            
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])


    return max(triangle[n-1])