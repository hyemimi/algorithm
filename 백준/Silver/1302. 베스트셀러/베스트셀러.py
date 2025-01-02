n = int(input())

dic = {}

for _ in range(n):
    a = input()

    if a in dic:
        dic[a] += 1
    else :
        dic[a] = 1


max_value = max(dic.values()) # 최대 값
max_keys = [key for key, value in dic.items() if value == max_value]

# 사전순으로 가장 앞선 키 선택
max_key = min(max_keys)

print(max_key)