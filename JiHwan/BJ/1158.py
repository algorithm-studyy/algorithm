from collections import deque

num , pop_num = map(int,input().split())
queue = deque()

for i in range(1,num+1):
    queue.append(i)


while(len(queue)!=0):
    queue.rotate(-(pop_num))
    r = queue.pop()
    print(r)


