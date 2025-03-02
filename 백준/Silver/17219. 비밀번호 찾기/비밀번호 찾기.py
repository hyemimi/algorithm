import sys

n,m = map(int,sys.stdin.readline().split())
memo = {}

for i in range(n):
    site, password = sys.stdin.readline().split()
    
    memo[site] = password


for j in range(m):
    target = sys.stdin.readline().rstrip()

    print(memo[target])