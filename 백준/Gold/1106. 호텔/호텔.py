c,n = map(int,input().split()) # c명 늘려야 함, n개의 도시
arr = []

for i in range(n):
    p, v = map(int,input().split()) # p는 비용, v는 얻을 수 있는 고객 수
    arr.append((p,v))


# 정수배 선택 가능. 9원, 3명 유치 -> 18원, 6명 유치 등
# 최솟값 구하기


MAX = c + 100 * n
dp = [int(1e9)] * (MAX) # dp[i]는 i명을 늘릴 때 내야 하는 비용
dp[0] = 0

for i in range(n):
    price, number = arr[i]

    for j in range(number,MAX):
        dp[j] = min(dp[j],dp[j-number] + price)


ans = dp[c:] # 적어도 c명 이상이므로 c부터 

print(min(ans))