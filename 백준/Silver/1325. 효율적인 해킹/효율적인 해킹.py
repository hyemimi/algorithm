from collections import deque
n,m = map(int,input().split())

graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v2].append(v1)


def BFS(v):

    visited = [False] * (n+1) # 각 노드 별로 방문 배열 선언
    visited[v] = True
    
    queue = deque()
    queue.append(v)

    cnt = 1 # 해킹 시키는 컴퓨터의 갯수

    while (len(queue) > 0) :
        vertex = queue.popleft()

        for ele in graph[vertex]:

            if not visited[ele] :
                # 방문 안 했을 경우 방문
                visited[ele] = True
                queue.append(ele)
                cnt += 1

    return cnt

ans = -1
arr = []
    
for i in range(1,n+1):

    # 각 노드 별로 해킹 가능 여부를 검사 
    result = BFS(i)

    if result > ans:
        ans = result
        arr = [i]  # 최대값 갱신 시 결과 초기화
    elif result == ans:
        arr.append(i)  # 최대값과 같으면 추가

arr.sort()
print(*arr)

