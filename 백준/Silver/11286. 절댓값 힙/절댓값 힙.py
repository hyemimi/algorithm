import heapq

n = int(input())

queue = []

for i in range(n):
    a = int(input())

    if a == 0:
        # 가장 작은 절댓값을 출력하고 배열에서 제거
        if len(queue) == 0 :
            print(0)
        else :
            print(heapq.heappop(queue)[1])
    else :
        # 배열에 추가

      
        heapq.heappush(queue,(abs(a),a))
