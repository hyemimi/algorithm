t = int(input())


while (t > 0) :

    stack = []
    str = input()
    ans = 'YES'

    for l in str:

        if l == '(' :
            stack.append('(')
        elif l == ')':

            if len(stack) > 0:
                a = stack.pop()

            else :
                # 스택이 비어 있음
                ans = 'NO'
                break
    
    if len(stack) > 0:
        ans = 'NO'
    
    print(ans)

    t -= 1