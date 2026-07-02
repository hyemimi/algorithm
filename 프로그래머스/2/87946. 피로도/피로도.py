def solution(k, dungeons):
    answer = -1
    
    # 탐험할 수 있는 최대 던전 수
    # DFS depth 사용
    # 백트래킹
    n = len(dungeons)
    visited = [0] * (n)
    
    def DFS(total, cnt): # 현재 체력, 방문했던 던전 수 (차수)
        
        nonlocal answer
        
        answer = max(answer, cnt)
        
        for j in range(n):
            
            need, spend = dungeons[j]
            
            if total >= need and visited[j] != 1:
                visited[j] = 1
                DFS(total - spend, cnt+1)
                visited[j] = 0 # 백트래킹
    
        
    DFS(k, 0)
    
    return answer