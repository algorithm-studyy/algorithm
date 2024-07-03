from sys import stdin
from collections import deque


def is_bigger(a, b):
    if a > b:
        return False
    else:
        return True


def stand_in_line():
    ns = deque([])
    result = 0
    for s in st:
        ns.appendleft(s)
        for i in range(len(ns) - 1):
            if is_bigger(ns[i], ns[i + 1]):
                ns[i], ns[i + 1] = ns[i + 1], ns[i]
                result += 1
            else:
                break
    print(f'{t} {result}')


for _ in range(int(stdin.readline())):
    line = list(map(int, stdin.readline().split()))
    t, st = line[0], deque(line[1:])
    stand_in_line()
