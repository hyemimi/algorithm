from collections import deque

def solution(cacheSize, cities):
    answer = 0
    n = len(cities)
    
    queue = deque([(cities[0].lower())])
    answer += 5
    
    if cacheSize == 0:
        return len(cities) * 5
    
    def isCacheHit(queue, city):
        for item in queue:
            if item == city:
                return True
        
        return False
        

    for i in range(1,n):
        city = cities[i].lower()
        
        # 캐시 히트일 경우
        if isCacheHit(queue, city):         
            answer += 1
            queue.remove(city)
            queue.append(city)
        
        # 캐시 미스
        else:
            answer += 5
            queue.append(city)
            
        if len(queue) > cacheSize:
            queue.popleft().lower()

    
    return answer