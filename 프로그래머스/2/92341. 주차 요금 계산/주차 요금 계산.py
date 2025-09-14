import math 

def solution(fees, records):
    
    
    # fees 기본 시간 / 기본 요금 / 단위 시간 / 단위 요금
    # 기본 시간 초과 시 기본 요금 + Math.ceil((누적 주차 시간-기본 시간)/단위 시간) *단위 요금
    
    defaultTime, defaultFee, unitTime, unitFee = fees
    
    cars = {}
    
    def convertTextToValue(str):
        time = str[0:5]
        number = str[6:10]
        type = str[13:15]
        return time,number,type
    
    # Records 돌면서 번호를 key에 값으로 [입차,출차,입차,...] 기록
    for i in range(len(records)):
        
        time, number, type  = convertTextToValue(records[i])
        
        if number in cars:
            cars[number].append(time)
        else :
            cars[number] = [time]
    print(cars)
    newCars = dict(sorted(cars.items()))
   
    # cars 돌면서 자동차 별로 청구 금액 append
    
    def diffMinutes(IN,OUT):
        return ((int(OUT[0:2]) - int(IN[0:2])) * 60) + (int(OUT[3:5]) - int(IN[3:5]))
    
    def calculatePrice (minutes):
        
        if defaultTime < minutes:
            return defaultFee + math.ceil((minutes - defaultTime) / unitTime) * unitFee
        
        else :
            return defaultFee 
        
    answer = []
    for key in newCars:
        times = newCars[key]
        
        if len(times) % 2 == 1:
            times.append('23:59')
            
        tempMinutes = 0

        while(len(times) > 0):
            
            IN = times.pop(0)
            OUT = times.pop(0)
            tempMinutes += diffMinutes(IN,OUT)
            
        answer.append(calculatePrice(tempMinutes))
    
    return answer