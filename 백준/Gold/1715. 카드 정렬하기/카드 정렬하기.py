import heapq

n = int(input()) # 최소 비교 횟수 
pq = []

# 최소로 합치는 경우의 합 (두 묶음씩 고름)
# (10+20) + (30+40) = 100
# 10-20, 30-40 // 10-30, 20-40, // 10-40 , 20-30 // 
for i in range(n):
    a = int(input())
    heapq.heappush(pq,a)


ans = 0

# pq의 길이가 2 이상일 때 수행 
while(len(pq) > 1):
    # 가장 작은 값 두 개를 더해서 우선순위 큐에 넣음 
    Sum = heapq.heappop(pq) + heapq.heappop(pq)
    ans += Sum

    heapq.heappush(pq,Sum) # 다시 heap에 삽입 
    

print(ans)

    
   