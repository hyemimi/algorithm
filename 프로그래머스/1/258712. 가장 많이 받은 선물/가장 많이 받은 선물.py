def solution(friends, gifts):
    answer = 0
    
    # 주고 받은 기록이 없거나, 같은 수로 주고 받으면 -> 선물지수
    # 준 선물 +, 받은 선물 - = 선물지수
    # 선물지수가 큰 애가 선물을 받음, 선물지수도 같으면 아예 둘다 x
    
    # 이름 -> index로 변경해 dict에 저장
    n = len(friends)
    
    dict = {}
    for i, name in enumerate(friends):
        dict[name] = i
        
    # 2차원 배열로 선물 준 것 기록
    board = [[0] * (n) for _ in range(n)]
    
    for gift in gifts:
        sender, receiver = gift.split()
        
        board[dict[sender]][dict[receiver]] += 1
    
    # 선물 지수: 선물 준 횟수 - 받은 횟수
    def getGiftNum():
        giftNum = [0] * (n)
        
        # 준 횟수
        for i in range(n):
            for j in range(n):
                giftNum[i] += board[i][j]      

        for i in range(n):
            for j in range(n):
                
                if j == i:
                    continue
                    
                giftNum[i] -= board[j][i]
        
        return giftNum

    
    # 선물을 받는 친구 계산
    temp = [0] * (n)
    giftNum = getGiftNum()
    print(giftNum)
    
    for i in range(n):
        for j in range(i+1, n):
            
            if board[i][j] > board[j][i]:
                # 선물을 더 많이 줬으므로 받음
                temp[i] += 1
            
            elif board[i][j] < board[j][i]:
                temp[j] += 1
                
            else :
                # 서로 주고 받은 선물 횟수가 같음
                # 선물 지수 판단
                if giftNum[i] > giftNum[j]:
                    temp[i] += 1
                elif giftNum[i] < giftNum[j]:
                    temp[j] += 1
                else:
                    # 아무도 안 받음
                    continue     

    
    return max(temp)