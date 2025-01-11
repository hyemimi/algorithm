n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = int(1e9)

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(n):
    for j in range(n):
        if graph[i][j] == int(1e9):
            graph[i][j] = 0
            continue
        elif graph[i][j] > 0:     
            graph[i][j] = 1  
           

for row in graph:
    print(" ".join(map(str, row)))

