# 최대 공약수 = 나눠지는 수 중 가장 큰 공약수
# 최소 공배수 = 곱해지는 수 중 가장 작은 공배수
from sys import stdin


# def get_line_input():
#     n = int(stdin.readline())
#     for _ in range(n):
#         line = stdin.readline()
#         solution(line)


def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    solution(a, b)


def solution(a, b):
    gcd = 1
    min_value = min(a, b)
    max_value = max(a, b)
    for i in range(1, min_value + 1):
        if min_value % i != 0:
            continue
        val = min_value // i
        if max_value % val == 0:
            gcd = val
            break
    lcd = (min_value // gcd) * (max_value // gcd) * gcd
    print(gcd, lcd, sep='\n', end='')


get_two_input()
