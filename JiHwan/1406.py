import sys

sentence = list(input())
num = int(input())
stack = []


for i in range(num):
    order = sys.stdin.readline().split()

    if order[0] == 'P':
        sentence.append(order[1])
    elif order[0] == 'L' and sentence:
        stack.append(sentence.pop())
    elif order[0] == 'D' and stack:
        sentence.append(stack.pop())
    elif order[0] == 'B' and sentence:
        sentence.pop()
    else:
        continue

print(''.join(sentence + stack[::-1]))
    
