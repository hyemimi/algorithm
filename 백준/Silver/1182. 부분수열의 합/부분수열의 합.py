n, s = map(int,input().split())

# n개의 수들 중에서 합이 s가 되는 부분 수열의 개수

target = list(map(int,input().split()))

cnt = 0

# idx : n개의 수들까지만 검사
def dfs(idx,current_sum):

    global cnt

    if idx == n:
        if current_sum == s:
            cnt += 1
        return
    
    
    dfs(idx+1,current_sum + target[idx])
    dfs(idx+1,current_sum)


dfs(0,0)

if (s==0):
    cnt -= 1

print(cnt)