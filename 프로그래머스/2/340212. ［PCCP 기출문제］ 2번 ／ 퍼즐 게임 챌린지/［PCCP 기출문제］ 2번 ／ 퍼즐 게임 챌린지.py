def solution(diffs, times, limit):
    answer = int(1e9)
    n = len(diffs)
    
    # 숙련도의 최솟값 구하기
    def calTime(level, diff, time_prev, time_cur):
        # 숙련도에 따른 퍼즐 게임 해결 시간 계산
        
        if diff <= level:
            return time_cur
        
        elif diff > level:
            return (time_prev + time_cur) * (diff-level) + time_cur
        
        
    # 숙련도 최솟값 구하기 -> level이 클수록 총 걸리는 시간이 작아짐. 이분탐색
    
    left = 1
    right = max(diffs)
    
    while (left <= right):
        mid = (left + right) // 2
        total = 0
        
        for j in range(n):
            
            if j == 0:
                total += calTime(mid, diffs[j], 0, times[j]) 
            else :           
                total += calTime(mid, diffs[j], times[j-1], times[j]) 
        
        if total <= limit:
            # 제한시간 안에 풀 수 있음
            answer = mid
            right = mid - 1
        else :
            left = mid + 1

    
    return answer