# 최대 공약수 = 나눠지는 수 중 가장 큰 공약수
# 최소 공배수 = 곱해지는 수 중 가장 작은 공배수
from sys import stdin


def get_line_input():
    n = int(stdin.readline())
    for _ in range(n):
        solution()


def solution():
    a, b = map(int, stdin.readline().split(" "))
    gcd = get_gcd(a, b)
    print((a * b) // gcd)


def get_gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


get_line_input()
