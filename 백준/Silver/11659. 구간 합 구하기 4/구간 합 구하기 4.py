import sys
input = sys.stdin.readline

# O(n+m)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pre = [0]
ans = 0

# 누적합 구하기 
for i in range(n):
  ans += arr[i]
  pre.append(ans)


# 누적합 사용해 구하기. 2-4 이면 4번째 인덱스 값에서 첫 번째 인덱스 값을 빼줌 
for i in range(m):
  a, b = map(int, input().split())
  print(pre[b] - pre[a-1])