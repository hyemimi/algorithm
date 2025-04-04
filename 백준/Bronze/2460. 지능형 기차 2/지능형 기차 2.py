
# 기차에 사람이 가장 많을 때의 사람 수
# 내리고, 탄 사람 더해서 카운팅

cnt = 0
current = 0


for i in range(10):
    down, up = map(int,input().split())
    current = (current - down) + up
    cnt = max(cnt, current)

print(cnt)