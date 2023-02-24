from sys import stdin

num = 0


def get_line_input():
    n = int(stdin.readline())
    for _ in range(n):
        line = stdin.readline().strip()
        solution(line)


def solution(line):
    global num
    line = line.split(' ')
    if line[0] == 'add':
        num = num | (1 << (int(line[1]) - 1))
    elif line[0] == 'check':
        if num & (1 << (int(line[1]) - 1)):
            print('1')
        else:
            print('0')
    elif line[0] == 'remove':
        num = num & ~(1 << (int(line[1]) - 1))
    elif line[0] == 'toggle':
        num = num ^ (1 << (int(line[1]) - 1))
    elif line[0] == 'all':
        num = (1 << 20) - 1
    else:
        num = 0


get_line_input()
