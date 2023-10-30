# R(뒤집기), D(버리기)
from sys import stdin
from collections import deque


def get_processing_command(command):
    return command.replace('RR', '')


def solution(command, arr):
    direction = 'L'
    for c in command:
        if c == 'R':
            direction = 'R' if direction == 'L' else 'L'
        else:
            if arr:
                if direction == 'L':
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                return
    if direction == 'R':
        arr.reverse()
    print(f"[{','.join(arr)}]")


def main():
    for _ in range(int(stdin.readline())):
        command = get_processing_command(stdin.readline().strip())
        length = int(stdin.readline())
        arr_str = stdin.readline().strip()[1:-1]
        arr = list(arr_str.split(",")) if arr_str else []
        solution(command, deque(arr))
        

main()
