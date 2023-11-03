import sys
from collections import deque

size = int(input())
a_list =deque()

for i in range(size) : 
    order = sys.stdin.readline().split()
    # 테스트
    if order[0]=="push_back":
        a_list.append(order[1])
        #print(a_list)
    if order[0]=="push_front":
        a_list.appendleft(order[1])
        #print(a_list)
    if order[0]=="pop_front":
        if len(a_list) !=0 : print(a_list.popleft())
        else : print(-1)
    if order[0]=="pop_back":
        if len(a_list) !=0 : print(a_list.pop())
        else : print(-1)
    if order[0]=="size":
        print(len(a_list))
    if order[0]=="empty":
        if len(a_list) !=0 : print(0)
        else : print(1)
    if order[0] == "front":
        if len(a_list) !=0 : print(a_list[0])
        else : print(-1)
    if order[0]=="back":
        if len(a_list) !=0 : print(a_list[len(a_list)-1])
        else : print(-1)