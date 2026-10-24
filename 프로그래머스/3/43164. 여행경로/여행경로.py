def solution(tickets):
    answer = []
    
    # [a, b] a에서 b로 가는 항공권이 있다
    # 같은 도시를 여러번 반복함.
    
    # 도시 별 이동 해시
    dic = {}

    for i, ticket in enumerate(tickets):
        a, b = ticket
        
        if a in dic:
            dic[a].append((i,b))
        else:
            dic[a] = []
            dic[a].append((i,b))
    
    
    # 총 방문해야 하는 도시의 갯수
    n = len(tickets)
    
    visited = set()
    temp = ["ICN"]
    

    def DFS(city):
        
        # 전부 방문
        if len(temp) == n + 1 :
            answer.append(temp[:])
            return

        for nextCity in dic.get(city, []):
            idx, city = nextCity
            
            # 이미 방문했던 경우
            if idx in visited:
                continue
            
            visited.add(idx)
            temp.append(city)
            DFS(city)
            visited.remove(idx)
            temp.pop()
        
    
    DFS("ICN")
    m = len(answer)
    
    if m == 1:
        return answer[0]
    
    answer.sort()
    
    return answer[0]
    
    
    return answer