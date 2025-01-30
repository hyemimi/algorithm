n = int(input())
w = []

# 로프가 버틸 수 있는 최대 무게? 
# 병렬로 나눌 수 있음 
# 모든 로프 사용할 필요 x

for i in range(n):
    w.append(int(input()))

w.sort()
# solution
## n=2일 경우, 로프 1개 사용 ~ 2개 사용까지 가능

ans = -1

for i in range(0,n):

    ans = max(ans,w[i] * (n-i))



print(ans)