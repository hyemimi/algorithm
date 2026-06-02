def solution(distance, rocks, n):
    answer = 0

    # 바위 n개 제거할 수 있는 경우의 수 중에서, 각 바위 사이의 거리들 중 최솟값이 가장 큰 경우
    # 출발 0, 도착지점 distance
    # 거리 기준으로 이분 탐색? - 최소 거리 mid가 가능한지
    left = 1
    right = distance
    
    rocks.sort()
    rocks.append(distance)
    
    while (left <= right):
        mid = (left + right) // 2
        prev = 0
        removed = 0
    
        for rock in rocks:
            
            if rock - prev < mid:
                # 최소거리보다 작으므로 제거해야 함
                removed += 1
            else :
                prev = rock
        
        if removed <= n:
            answer = mid
            left = mid + 1
        
        else:
            right = mid - 1
    
            
            
            
            
        
    
    
    
    return answer