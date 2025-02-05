n = int(input())
m = int(input())

graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

# 시작 도시, 도착 도시, 비용

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(m):
    a,b,c = map(int, input().split())

    # 노선이 여러 개일 수 있으므로, 최단 경로를 선택한다.
    if graph[a][b] > c:
        graph[a][b] = c



for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if j == k:
                graph[j][k]  = 0
                continue
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == int(1e9):
            print(0,end=" ")
        else :
            print(graph[i][j],end=" ")
    print(end="\n")