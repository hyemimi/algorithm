n = int(input())
card = list(map(int,input().split()))
m = int(input())
target= list(map(int,input().split()))

dict = {}

# O(n)
for j in range(n):
    dict[card[j]] = 1

# O(m)
for i in range(m):

    if target[i] in dict:
        print(1, end=" ")
    else:
        print(0,end= " ")

# O(n+m)


