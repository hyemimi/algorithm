A, B = map(int, input().split())

sequence = []
num = 1
while len(sequence) < B:
    sequence += [num] * num
    num += 1

print(sum(sequence[A-1:B]))