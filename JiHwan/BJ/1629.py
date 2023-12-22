import sys


def multi(x, y, z):
    if y == 1:
        return x % z
    result = multi(x, y // 2, z)
    if y % 2 == 0:
        return (result * result) % z
    else:
        return ((result * result) * x) % z


if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    print(multi(a, b, c))
