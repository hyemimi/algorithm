
# input :: 첫째 줄에 1번 톱니바퀴의 상태, 
# 둘째 줄에 2번 톱니바퀴의 상태, 
# 셋째 줄에 3번 톱니바퀴의 상태, 
# 넷째 줄에 4번 톱니바퀴의 상태

arr = [list(map(int, input())) for _ in range(4)]
k = int(input())
rotation = [tuple(map(int, input().split())) for _ in range(k)]

# 톱니바퀴를 시계 방향으로 회전
def rotate(num):
    tmp = arr[num][7]
    for i in range(7, 0, -1):
        arr[num][i] = arr[num][i - 1]
    arr[num][0] = tmp

# 톱니바퀴를 반시계 방향으로 회전
def rotateReverse(num):
    tmp = arr[num][0]
    for i in range(7):
        arr[num][i] = arr[num][i + 1]
    arr[num][7] = tmp

# 회전 처리
for ele in rotation:
    num = ele[0] - 1 # 톱니바퀴 번호 (1 ~ 4이지만 arr에 맞춰 0부터 시작)
    direction = ele[1]  # 회전 방향 (1: 시계, -1: 반시계)

    # 회전 방향 저장
    rotate_directions = [0] * 4
    rotate_directions[num] = direction

    # 왼쪽
    for i in range(num - 1, -1, -1):
        if arr[i][2] != arr[i + 1][6]:  # 인접 톱니바퀴의 극 비교
            rotate_directions[i] = -rotate_directions[i + 1]
        else:
            break

    # 오른쪽
    for i in range(num + 1, 4):
        if arr[i - 1][2] != arr[i][6]:  # 인접 톱니바퀴의 극 비교
            rotate_directions[i] = -rotate_directions[i - 1]
        else:
            break

    # 회전 적용
    for i in range(4):
        if rotate_directions[i] == 1:
            rotate(i)
        elif rotate_directions[i] == -1:
            rotateReverse(i)

# 점수 계산
Sum = 0
for i in range(4):
    if arr[i][0] == 1:  # 12시 방향이 S극이면 점수 추가
        Sum += 2**i # 첫 번째 톱니바퀴 2**0, 두 번째 2**1 , ... 

print(Sum)