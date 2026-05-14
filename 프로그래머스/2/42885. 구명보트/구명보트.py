def solution(people, limit):
    answer = 0
    n = len(people)
    
    # 한 번에 최대 2명씩, 최대한 많은 사람 태움.
    # 구명 보트 최대한 적게 사용
    # people 오름차 순 정렬 후, 가벼운 사람은 무거운 사람과 보트를 태움.
    
    people.sort()
    
    left = 0
    right = n - 1 
    
    while (left <= right):
        
        if (people[left] + people[right] <= limit):
            left += 1
        
        answer += 1
        right -= 1
        
  
    
    return answer