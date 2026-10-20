def solution(routes):
    
    # 모든 차량이 한 번은 단속 카메라를 만나야 함.
    # 최소 몇 대의 카메라를 설치해야 하는지
    
    n = len(routes)
    ans = 0
    
    routes.sort(key = lambda x: (x[1], x[0]))
    
    cur = routes[0][1]
    ans += 1
    
    for i in range(1, n):
        start, end = routes[i]
        
        if start > cur:
            # 카메라 만나지 않음 -> 새로 설치
            cur = end
            ans += 1

    
    return ans