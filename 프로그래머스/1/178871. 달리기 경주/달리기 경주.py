def solution(players, callings):
    answer = []
    
    
    # players 기반으로 Map 구성
    dict = {}
    for idx, player in enumerate(players):
        dict[player] = idx

    # O(1,000,000)
    for calling in callings:
        
        currentRank = dict[calling] # 등수
        previousPlayer = players[currentRank - 1] # 이름
        
        dict[calling] = currentRank - 1
        dict[previousPlayer] = currentRank
        
        players[currentRank] = previousPlayer
        players[currentRank-1] = calling 


    return players