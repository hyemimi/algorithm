def solution(n, costs):
    answer = 0
    
    # 최소 비용으로 모든 섬들을 연결함.
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    
    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        
        return parent[a]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        
        if a == b:
            return False
        
        if rank[a] > rank[b] :
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else :
            parent[a] = b
            rank[b] += 1
        
        return True
    
    answer = 0
    
    costs.sort(key=lambda x: x[2])
    
    for cost in costs:
        
        if (union(cost[0], cost[1])):
            # 연결됨
            answer += cost[2]
        
    
    return answer