def solution(board, skill):
    answer = 0
    
    # 최종적으로 내구도가 1 이상이면 파괴 x
    # skill [type, r1, c1, r2, c2, degree]
    # type이 1이면 적의 공격 / type이 2이면 아군의 회복
    # skill을 돌면서 board를 갱신함. 
    
    n = len(board)
    m = len(board[0])
    
    diff = [[0] * (m+1) for _ in range(n+1)]    
    # 스킬 적용
    for i in range(len(skill)) :
        type, r1, c1, r2, c2, degree = skill[i]
        
        if type == 1:
            degree = -degree
        
        diff[r1][c1] += degree
        diff[r1][c2+1] -= degree
        diff[r2+1][c1] -= degree
        diff[r2+1][c2+1] += degree
    
    # 행 누적합
    for i in range(n):
        for j in range(m):
            diff[i][j+1] += diff[i][j]
    
    # 열 누적합
    for j in range(m):
        for i in range(n):
            diff[i+1][j] += diff[i][j]
    
    

    # # 카운트
    for i in range(n):
        for j in range(m):
            if diff[i][j] + board[i][j] > 0 :
                answer += 1    

    return answer