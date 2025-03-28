n = int(input()) # 원판의 갯수
moves = [] # 이동 루트

def hanoi (n,start,end,via) :

    if n == 1:
        moves.append((start,end))
        return
    
    hanoi(n-1,start,via,end)
    moves.append((start,end))
    hanoi(n-1,via,end,start)

hanoi(n,1,3,2)
s = len(moves)
print(s)

for i in range(s):
    print(moves[i][0],moves[i][1])