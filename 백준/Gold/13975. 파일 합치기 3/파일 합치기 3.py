import heapq

t = int(input())

while(t > 0):

    n = int(input())
  
    pq = list(map(int,input().split()))
    heapq.heapify(pq)
    temp = 0


    while (len(pq) > 1) :
        Sum = heapq.heappop(pq) + heapq.heappop(pq)
        temp += Sum
        heapq.heappush(pq,Sum)
    
    print(temp)



    t -= 1