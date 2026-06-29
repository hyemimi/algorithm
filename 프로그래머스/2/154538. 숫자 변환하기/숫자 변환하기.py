from collections import deque

def solution(x, y, n):
    answer = 0
    queue = deque([(x, 0)])
    visit = [0] * (y+1)
    visit[x] = 1
    
    while (queue):  
        num, cnt = queue.popleft()
        
        if num == y:
            return cnt
        
        
        if 1 <= num+n <= y and visit[num+n] != 1:
            queue.append((num+n,cnt+1)) 
            visit[num+n] = 1
        if 1 <= num*2 <= y and visit[num*2] != 1:
            queue.append((num*2, cnt+1))
            visit[num*2] = 1
        if 1 <= num*3 <= y and visit[num*3] != 1: 
            queue.append((num*3, cnt+1))
            visit[num*3] = 1
    
    return -1

    return answer