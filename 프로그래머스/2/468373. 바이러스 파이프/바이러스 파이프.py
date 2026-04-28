from collections import deque

def solution(n, infection, edges, k):
    answer = 1

    graph = [[] for _ in range(n + 1)]

    # 그래프 저장
    for edge in edges:
        x, y, edge_type = edge
        graph[x].append((y, edge_type))
        graph[y].append((x, edge_type))

    # 상태:
    # 현재 감염된 노드들, 감염 여부, 지금까지 연 횟수
    queue = deque()

    infected = [0] * (n + 1)
    infected[infection] = 1

    queue.append(({infection}, infected, 0))

    while queue:
        current_nodes, infected, open_count = queue.popleft()

        answer = max(answer, sum(infected))

        if open_count == k:
            continue

        # 이번 턴에 1, 2, 3 중 하나의 파이프를 연다
        for open_type in [1, 2, 3]:
            next_infected = infected[:]
            next_nodes = set(current_nodes)

            bfs = deque(current_nodes)

            while bfs:
                x = bfs.popleft()

                for y, edge_type in graph[x]:
                    if edge_type != open_type:
                        continue

                    if next_infected[y]:
                        continue

                    next_infected[y] = 1
                    next_nodes.add(y)
                    bfs.append(y)

            queue.append((next_nodes, next_infected, open_count + 1))

    return answer
