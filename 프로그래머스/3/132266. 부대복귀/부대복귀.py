from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n + 1)
    dist[destination] = 0
    
    queue = deque([destination])
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                queue.append(next_node)
    
    return [dist[source] for source in sources]