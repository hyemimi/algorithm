def solution(routes):
    n = len(routes)
    
    # in, out
    # 모든 차량이 단속용 카메라를 만나야 함.
    # 최소 몇 대의 카메라를 설치해야 하는지? -> 초반에 
    
    routes.sort(key=lambda x:x[1])
    
    camera = routes[0][1] # (초기화) 첫 진출 지점에 카메라 설치
    answer = 1
    
    for route in routes:
        start, end = route[0], route[1]
        
        if start <= camera <= end:
            # 카메라 설치하지 않아도 됨.
            continue
        
        else :
            # 카메라 새로 설치
            camera = end
            answer += 1

    
    
    return answer