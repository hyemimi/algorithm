def solution(n, times):
    answer = 0
    
    # 비어 있는 심사대에서 심사 받되, 더 빨리 끝나는 심사대가 있다면 기다림
    # 모든 사람이 심사를 받는데 걸리는 총 시간 최소화
    # 파라메트릭 서치 문제 -> 시간을 기준으로
    
    left = 1
    right = max(times) * n
    
    while (left <= right):
        mid = (left + right) // 2
        
        count = 0
        for time in times:
            # mid 시간 안에 몇 명을 심사할 수 있는지 계산
            count += mid // time
        
        if count >= n:
            # 모두 심사할 수 있음
            answer = mid
            right = mid - 1
        
        elif count < n:
            # 부족함
            left = mid + 1

        
        
    
    
            
    
    
    return answer