# 무게가 중간이 될 수 없는 구슬의 수 출력

n, m = map(int,input().split()) # 구슬의 갯수, 저울 쌍 수
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int,input().split())

    # 앞 번호 구슬이 더 무겁다
    graph[node1][node2] = 1

for k in range(1,n+1):
    graph[k][k] = 0

ans = 0
middle =  (n+1) // 2

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n+1):
    heavy, light = 0, 0

    for j in range(1, n+1):

        if i != j :

            if graph[i][j] != int(1e9):  # i가 더 무겁다 
                heavy += 1
            if graph[j][i] != int(1e9):  # j가 더 무겁다
                light += 1

    # 절반 이상보다 무겁거나 가벼우면 중간 무게 불가능
    if heavy >= middle or light >= middle:
        ans += 1


print(ans)