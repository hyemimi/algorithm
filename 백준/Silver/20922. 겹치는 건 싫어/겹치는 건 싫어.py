n, k = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = 0
count = {}  # 숫자의 빈도 저장 (딕셔너리)
max_length = 0

while rt < n:
    
    if arr[rt] in count:
        # 이미 존재함 
        count[arr[rt]] += 1
    else:
        # 존재하지 않음 (초기화)
        count[arr[rt]] = 1

    # 중복되는 수 k개 초과 
    while count[arr[rt]] > k:
        count[arr[lt]] -= 1

        # 0의 값 => 딕셔너리에서 제거 
        if count[arr[lt]] == 0:
            del count[arr[lt]]
        lt += 1

    # 현재 부분 수열의 길이 계산
    max_length = max(max_length, rt - lt + 1)

    # 오른쪽 포인터 이동
    rt += 1

print(max_length)
