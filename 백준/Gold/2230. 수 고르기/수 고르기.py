import sys

n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

lt = 0
rt = 0

minMinus = sys.maxsize

while( rt < n) :
    minus = arr[rt] - arr[lt]

    if (minus >= m):
        # 차이가 m 이상임 => 차이의 최솟값을 구해야 하므로, lt += 1 

        minMinus = min(minMinus,minus)
        lt += 1

        if lt > rt:  # lt가 rt를 초과하면 rt를 맞춰줌
            rt = lt

    else :
        rt += 1



print(minMinus)