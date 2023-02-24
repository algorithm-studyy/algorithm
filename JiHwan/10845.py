import sys

size = int(sys.stdin.readline()) 
queue = []

for i in range(size) : 
    order = sys.stdin.readline().split()

    if order[0]=="push":
        queue.append(order[1])
        
    if order[0]=="pop":
        if len(queue) !=0: print(queue.pop(0))
        else : print(-1)
    if order[0]=="empty":
        if len(queue) !=0 : print(0)
        else : print(1)
    if order[0]=="size":
        print(len(queue))
    if order[0]=="front":
        if len(queue)!=0 : print(queue[0])
        else : print(-1)
    if order[0]=="back":
        if len(queue)!=0 : print(queue[len(queue)-1])
        else : print(-1)