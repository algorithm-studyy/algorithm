razor = list(input())
result = 0
stack = []

for i in range(len(razor)):
    if razor[i] == '(':
        stack.append(razor[i])

    else :
        if razor[i-1] == '(':
            stack.pop()
            result +=len(stack)
        else:
            stack.pop()
            result += 1
print(result)