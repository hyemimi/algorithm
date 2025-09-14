from itertools import product

def solution(users, emoticons):
    answer = []
    # 이모티콘 서비스 가입 -> 각각 사용자마다 정한 기준 이상이면 가입
    # 할인율은 10, 20, 30, 40 % 중 하나. 
    # 이모티콘은 할인율 이상이면 모두 구매
    # 이모티콘 서비스 가입자를 최대한 늘리고, 아니라면 이모티콘 판매액을 늘린다 (가입 안한 사용자가 지불한 비용)
    
    def discountPrice(percent,price): 
        return int(price - (price * percent / 100))
    
    # emoticons의 갯수만큼 4Cn을 해서 경우의 수를 구하고, 근데 여기서 중복 순열이다
    # 그 경우의 수를 돌면서, users 배열을 돌고, 해당 배열 내에서 기준 값(users[i][1])이 초과하면 가입자 수 증가. 초과하지 않는다면 이모티콘 판매액에 합산
    cases = []
    n = len(emoticons)
    
    for i in product([10,20,30,40],repeat=n):
        cases.append(i)
        
   
    
    for case in cases :
        
        join = 0 # 가입한 사용자 수
        total = 0
        
        for i in range(len(users)):
            
            userTotalPrice = 0

            for j in range(len(emoticons)):
                if users[i][0] > case[j]:
                    # 원하는 할인율 미만이면
                    continue

                userTotalPrice += discountPrice(case[j],emoticons[j])
            
            if userTotalPrice >= users[i][1] :
                join += 1
            else :
                total += userTotalPrice
            
        answer.append([join,total])         
        
        
       
        
    answer = sorted(answer, key=lambda x: (x[0], x[1]), reverse=True)
    
    
    return answer[0]