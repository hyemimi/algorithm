import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    # k 미만인 최솟값 2개를 뽑아서 섞는다.
    # 최소힙?
    
    while (scoville):
     
            a = heapq.heappop(scoville)

            if a < K:
                # 섞어야됨
                if not scoville: return -1
                b = heapq.heappop(scoville)   
                heapq.heappush(scoville, a+(b*2))   
                answer += 1
                
            else:
                # 이미 충족
                return answer

    
    return -1