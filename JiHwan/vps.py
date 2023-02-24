num = int(input())

for i in range(num):
    stack = []
    vpc=input()
    for j in vpc:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: 
                print("NO")
                break
    else:
        if not stack: 
            print("YES")
        else:
            print("NO")