def solution(today, terms, privacies):
    answer = []
    
    # 모든 달은 28일까지 있다고 가정
    # (5월) 26 + (6월) 28 + (7월) 28 + (8월) 28 + (9월) 28 + (10월) 28 + (11월) 2일
    # 11월 1일까지 보관 가능, 2일부터 파기
    
    def convertTextToDate(str) :
        year = str[0:4]
        month = str[5:7]
        day = str[8:11]
        return int(year), int(month), int(day)
    
    year, month, day = convertTextToDate(today)
    
    def calculate(date, term):
        
        # terms 배열을 돌면서 해당하는 term을 찾고, 만료 기간 계산
        for i in range (len(terms)):
            category, months = terms[i].split(" ")
            
            if category == term :
                addMonth = months
                break
        
        year, month, day = convertTextToDate(date);

        for j in range(1,int(addMonth)+1):
            month = month + 1 # 6, 7, 8, 9, 10, 11

            if month > 12:
                year += 1
                month = 1

        return year, month, day
    
    # privacies 돌면서 만료 일자 구하기
    for k in range(len(privacies)):
        date, term = privacies[k].split(" ")
        calculateYear, calculateMonth, calculateDay = calculate(date, term)
        print(calculateYear,year, calculateMonth,month, calculateDay,day)
        
        if year > calculateYear :
            answer.append(k+1)
            continue    
        if year == calculateYear and month > calculateMonth :
            # 오늘 월이 더 크면 
            answer.append(k+1)
            continue
        if year == calculateYear and month == calculateMonth and day > calculateDay :
            answer.append(k+1)
        
        if year == calculateYear and month == calculateMonth and day == calculateDay :
            answer.append(k+1)
        
        
        
    
    

    return answer