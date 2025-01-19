
# p1, p2, p3 ... 각각은 가격. 인덱스는 카드팩 하나에 들은 카드의 갯수

n = int(input())  # 사야 하는 카드의 갯수
arr = list(map(int, input().split()))  # 카드팩 가격 리스트
dp = [0] * (n + 1)  #i개의 카드를 구매하는 최대 비용

# dp 계산
for i in range(1,n+1):  # 1부터 n개의 카드까지 dp 채움 
    for j in range(1,i+1):  
        # j개의 카드를 포함하는 카드팩 사용 

        if j <= len(arr):
            dp[i] = max(dp[i], dp[i-j] + arr[j-1])

print(dp[n])  # n개의 카드를 구매하는 최대 비용