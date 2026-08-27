import math

def solution(progresses, speeds):
    answer = []
    
    # 앞에서 다 안 끝나면 뒤의 작업들도 미뤄뒀다 같이 배포함
    # ( (100 - progress) / speed ) + 1 (딱 떨어지지 않을 경우) 일 동안 작업
    # 각 작업 일수 계산 후, 7, 3 이면 2개의 기능이 배포됨.
    
    n = len(progresses)
    
    # 1. progresses 돌면서 작업 일수 계산
    days = []
    for i in range(n):
        progress = progresses[i]
        speed = speeds[i]
        
        days.append(math.ceil((100 - progress) / speed))
    
    # 2. 작업 일수 돌면서 각 배포에 몇 개의 기능이 배포 가능한지 합산

    maxDay = days[0]
    cnt = 1
    for j in range(1, n):

        if maxDay >= days[j]:
            # 이번 배포에 포함
            cnt += 1
            
        else:
            maxDay = days[j]
            answer.append(cnt)
            cnt = 1
    
    answer.append(cnt)
            
    return answer