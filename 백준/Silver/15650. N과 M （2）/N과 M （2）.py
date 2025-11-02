n, m = map(int, input().split())

# n개의 수 중에서 m개를 중복없이 뽑는 수열 (경우의 수)


nums = []

def dfs(idx):

    if (len(nums) == m):
        # 다 선택함
        print(" ".join(map(str, nums)))
        return
    
    for i in range(idx+1,n+1):
        if i not in nums :
            # 이동 가능
            nums.append(i)
            dfs(i)
            nums.pop()

dfs(0)