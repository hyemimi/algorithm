arr = list(map(int,input()))


ans = 0
isReversed = False

for i in range(len(arr)-1):

    if isReversed==False and arr[i] != arr[i+1]:
        # 연속 시작 
        arr[i+1] = arr[i]
        ans += 1
        isReversed=True

    elif isReversed==True and arr[i] != arr[i+1]:
        # 연속중
        arr[i+1] = arr[i]
    
    else :
        isReversed = False
    


print(ans)