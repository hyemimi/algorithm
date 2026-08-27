def solution(want, number, discount):
    answer = 0
    
    # 매일 한 가지 할인, 10일동안 회원 자격 
    # want 항목들을 number 만큼 구매함
    # discount 돌면서 현재 타겟 일 + 10일 동안 want가 number 만큼 있는지 확인
    n = len(discount)
    
   
    # map에 want, number 기록
    dict = {}
    for idx, item in enumerate(want):
        dict[item] = number[idx]

    i = 0
    canDiscount = i + 10
    
    while(i < n):

        saved = {}
        
        # discount에서 want * number 만큼 살 수 있는지 확인
        for j in range(i, canDiscount):
            
            if j >= n:
                break 
            
            if (discount[j] in saved):
                saved[discount[j]] += 1
            else :
                saved[discount[j]] = 1

        # 만족하는지 확인
        flag = True
        for key in want:
      
            if key not in saved:
                # 없음
                flag = False
                break
            if saved[key] != dict[key]:    
                # 갯수가 다름
                flag = False
                break
        
        if flag:
            answer += 1

        i += 1
        canDiscount = i + 10
        
    
    return answer