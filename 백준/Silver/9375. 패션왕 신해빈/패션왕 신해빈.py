t = int(input())

while(t > 0):

    n = int(input())
    dict = {}
    result = 1

    for i in range(n):
        value, key = input().split()

        if key in dict:
            dict[key] += 1
        else :
            dict[key] = 1
        
    
    for i in dict:
        result *= dict[i] + 1 # 곱의 법칙, 안 입은 경우도 있으므로 1 더함 
    
    print(result - 1) # result가 1에서 시작했으므로 빼줌 

    t -= 1