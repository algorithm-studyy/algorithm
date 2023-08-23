import sys

size = int(sys.stdin.readline()) 
stack = []


for i in range(size) :
    sentence = input()
    sentence += " "
    for j in sentence:
        if j !=" ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(), end ='')
            print(' ', end = '')
