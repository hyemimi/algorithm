n = int(input())

ans = {}

# 딕셔너리 기록 
for i in range(n):
    name, status = input().split()

    ans[name] = status

# 딕셔너리 정렬: 키(이름)으로 내림차 순 정렬 후 리스트로 반환됨, 이를 딕셔너리로 전환 )
ans = dict(sorted(ans.items(),reverse=True))


# enter 상태 출력
for key,value in ans.items():

    if value == 'enter':
        print(key)
    