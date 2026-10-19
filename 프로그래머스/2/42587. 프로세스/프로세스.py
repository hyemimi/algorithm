from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque()
    
    for idx, pri in enumerate(priorities):
        queue.append((idx, pri))
      
    # 우선순위 큐 pop 하면서 실행 순서 기록
    ans = []
    while(queue):
        
        idx, pri = queue.popleft()
        
        if any(pri < p for _, p in queue):
            # 하나라도 우선순위가 큰 프로세스가 있다면 queue에 다시 삽입
            queue.append((idx, pri))
            
        else:
            # 현재 프로세스 실행
            answer += 1 # 실행한 프로세스 갯수 (= 실행 순서)
            
            if idx == location:
                return answer
    
  