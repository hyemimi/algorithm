import math 

# 에라토스테네스의 체
# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
# N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

n,k = map(int,input().split())
cnt = 0
check = [False] * (n+1);


for i in range(2, n+1) :
    
    if (check[i] == False) :
   
        for j in range (i, n+1, i) :

            if check[j] == False:
                check[j] = True
                cnt += 1

                if cnt == k:
                    print(j)

