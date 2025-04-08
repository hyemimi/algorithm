
arr = []
for i in range(9):
    arr.append(int(input()))


# 난쟁이 키 100 아홉 명중 7명 찾기

arr.sort()

def findTarget():

    current_sum = sum(arr)

    for i in range(0,9):
        current_sum = current_sum - arr[i]
        for j in range(0,9):
            if i!= j and current_sum - arr[j] == 100:

                return i,j

        current_sum += arr[i]


i,j = findTarget()

for k in range(9):
    
    if k != i and k != j:
        print(arr[k])
