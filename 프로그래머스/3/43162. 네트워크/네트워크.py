from collections import deque 

def solution(n, computers):
    answer = 0
    visit = [0] * (n+1)
    
    def bfs(node):
        queue = deque([(node)])
        visit[node] = 1
        
        while (queue):
            current = queue.popleft()
    
            for i in range(n):      
                if visit[i] != 1 and computers[current][i] == 1 :
                    # 방문하지 않은 경우 방문함
                    queue.append((i))
                    visit[i] = 1

    
    for i in range(n):
        
        if visit[i] != 1:
            bfs(i)
            answer += 1
        
      
    return answer