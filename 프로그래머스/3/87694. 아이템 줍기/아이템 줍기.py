from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y]
    # 테두리만 이동, 직사각형의 테두리만 graph에 저장
    # 다른 직사각형의 내부일 경우 pass 
    # 테두리는 1, 내부는 -1, 비어있는 공간은 0
    # 캐릭터가 이동해야 하는 가장 짧은 거리 구하기
    
    # 좌표 2배
    rectangle = [[x1 * 2, y1 *2, x2 * 2, y2 * 2] for x1, y1, x2, y2 in rectangle]
    characterX = characterX * 2
    characterY = characterY * 2
    itemX = itemX * 2
    itemY = itemY * 2
    
    # graph 저장
    graph = [[0] * (102) for _ in range(102)]
    n = len(rectangle)
    
    for i in range(n):
        x1, y1, x2, y2 = rectangle[i]
        
        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                
                if graph[j][k] == -1 :
                    # 겹쳐진 내부임
                    continue
                    
                elif x1 < j < x2 and y1 < k < y2:
                    # 내부
                    graph[j][k] = -1
                
                else:
                    graph[j][k] = 1
    
    queue = deque([(characterX, characterY, 0)])
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    while(queue):
        x, y, cnt = queue.popleft()
        
        if x == itemX and y == itemY:
            return cnt // 2
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]        
        
            if 0 <= nx < 102 and 0 <= ny < 102:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny, cnt + 1))
  

    
    return answer