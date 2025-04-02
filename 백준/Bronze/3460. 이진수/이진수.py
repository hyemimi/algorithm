t = int(input())

while(t) :
    n = int(input())
    binaryNum = format(n,'b')
  
    idx = 0

    for i in range(len(binaryNum)-1,-1,-1):

        if binaryNum[i] == '1':
            print(idx, end=" ")

        idx += 1    


    t -= 1
