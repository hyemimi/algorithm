t = int(input())


while(t > 0):
    n = int(input())

    arr = list(map(int,input().split()))

    # 매일 하는 것 -- 3 택 1
    # 주식 하나를 산다.
    # 원하는 만큼 가지고 있는 주식을 판다.
    # 아무것도 안한다

    # 3, 5, 9 일 시 3 + 5 = 8 / 18 - 8 = 10 이익
    max_price = 0
    profit = 0

    for i in range(n-1,-1,-1):
        
        if arr[i] > max_price:
            max_price = arr[i]
        else:
            profit += max_price - arr[i]

    print(profit)
    t -= 1
    # 6 7 10 