def solution(prices):
    n = len(prices)
    answer = [0] * (n)
    
    for i in range(n):
        price = prices[i]
        
        for j in range(i+1,n):
            answer[i] += 1
            
            if prices[j] < price:
                # 가격이 떨어짐
                break


    
    return answer