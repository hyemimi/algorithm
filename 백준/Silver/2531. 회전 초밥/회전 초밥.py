import sys
n,d,k,c = map(int,input().split()) # n: 접시의 수 , d: 초밥의 가짓수 , 연속해서 먹는 접시 수: k, 쿠폰 번호 : c

# 초밥을 먹는 최대 가짓수? 연속으로 k개 먹고 쿠폰 사용까지 하면 k+1개 먹을 수 있음
arr = []
food = {} # 빈도 저장 

for i in range(n):
    arr.append(int(input()))

Sum = 0
lt = 0
rt = 0

maxEat = -1

while (lt <n):

    Sum += 1

    if arr[rt] in food:
        food[arr[rt]] += 1
    else :
        food[arr[rt]] = 1
    
   
    while (Sum > k):
        Sum -= 1
        food[arr[lt]] -= 1
        
        if food[arr[lt]] == 0:
            # 딕셔너리에서 삭제 
            
            del food[arr[lt]]
        
        lt += 1

    
     # 연속으로 먹음 

    
    if Sum == k :
        # 쿠폰 사용 
        if c not in food:
            maxEat = max(maxEat, len(food)+1)
        
        # 쿠폰 해당 X 
        else :
            maxEat = max(maxEat, len(food))

    rt += 1

    if (rt == n):
        rt = 0




print(maxEat)
