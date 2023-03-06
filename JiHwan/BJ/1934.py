num = int(input())

def gdc(a, b):
    while b > 0:
        a, b = b, a % b
    return a



def lcm(a, b):
    return a * b // gdc(a, b)

for i in range(num):
    num1 ,num2 = map(int,input().split())
    print(lcm(num1, num2))
