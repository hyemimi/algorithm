str = input()
total = set() # 중복된 부분 문자열 방지 

for i in range(len(str)):
    # arr[i]부터 arr[j]까지의 부분 문자열 더하기
    for j in range(i,len(str)):
        total.add(str[i:j+1])
       
print(len(total))