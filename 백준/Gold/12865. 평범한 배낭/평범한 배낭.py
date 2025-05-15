n, k = map(int,input().split())
value = []

for i in range(n):
    w, v  = map(int,input().split());

    value.append((w,v))

# k 만큼의 무게를 넣을 수 있음
# 물건들의 가치 합의 최댓값
# knapsack

dp = [0] * (k+1) # dp[i] : i무게 까지의 가치 최댓값

for j in range(n):
    w, v = value[j]

    for i in range(k,w-1,-1):
        dp[i] = max(dp[i], dp[i-w] + v)
        

print(dp[k])