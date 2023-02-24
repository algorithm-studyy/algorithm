size = int(input())

stack = []
num = 0
answer = []
TF = "YES"

for i in range(size):
    x = int(input())

    while num < x:
        num += 1
        stack.append(num)
        answer.append('+')
        print(answer)
    
    if stack[-1] == x:
        stack.pop()
        answer.append('-')
        print(answer)
    
    else :
        TF = "NO"
        print(TF)
        break

if TF != "NO":
    for i in answer:
        print(i) 
    

