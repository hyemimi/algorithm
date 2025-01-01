from itertools import combinations

n, m = map(int,input().split())

# 0은 빈칸, 1은 집, 2는 치킨집
# 치킨집 중에서 M개를 고름(조합), 나머지 폐업할 때 최소 치킨 거리 출력

chicken = []
house = []

for r in range(n):
    arr = list(map(int,input().split()))

    for c in range(n):
        if arr[c] == 1:
            house.append((r,c))
        elif arr[c] == 2:
            chicken.append((r,c))

pickChickens = list(combinations(chicken,m))

def sumChickenDistance(cases):

    # 경우들을 기반으로 치킨 거리의 합 계산

    result = 0

    for nr,nc in house:
        # 집 마다 최소 치킨 거리의 합 구하기
        temp = int(1e9) 
        for nx,ny in cases:
            temp = min(temp, abs(nx - nr) + abs(ny - nc)) # 최소 치킨 거리 갱신
        
        result += temp

    return result




ans = int(1e9)

for pickChicken in pickChickens:
    
    result = sumChickenDistance(pickChicken)
    ans = min(result,ans) # 최소 거리의 합 갱신

print(ans)