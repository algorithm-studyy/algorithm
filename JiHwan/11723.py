import sys

n = int(input())

S = 0
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0]=='empty':
        S = 0
    elif order[0]=='all':
        S =(1<<20)-1
    else:
        command = order[0]
        num = int(order[1])-1
        if command=='add':
            if S &(1<<num):
                pass
            S |= 1 << num

        elif command=='remove':
            if S & (1 << num):
                S &= ~(1 << num)
            else:
                pass
        elif command=='check': # x가 있으면 1 없으면 0
            if S & (1<<num):
                print(1)
            else:
                print(0)
        elif command=='toggle': #x가 있으면 x를 제거, 없으면 x를 추가
            S ^= 1<<num