n = int(input())  # 레벨의 수
score = []

# 점수 입력 받기
for i in range(n):
    num = int(input())
    score.append(num)

ans = 0

# 뒤에서부터 앞으로 검사하면서 감소해야 하는 경우 처리
for i in range(n - 2, -1, -1):  # 뒤에서부터 검사
    if score[i] >= score[i + 1]:  
        ans += score[i] - (score[i + 1] - 1)  
        score[i] = score[i + 1] - 1  # 다음 레벨 점수보다 1 작게 설정

print(ans)