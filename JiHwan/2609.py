a, b = map(int, input().split())


def gdc(a, b):
    while b > 0:
        a, b = b, a % b
    return a



def lcm(a, b):
    return a * b // gdc(a, b)


print(gdc(a, b))
print(lcm(a, b))