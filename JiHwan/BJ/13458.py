n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
teacher = 0

for i in range(n):
    a[i] -= b
    if a[i] > 0:
        if a[i] % c != 0:
            teacher += a[i] // c + 1
        else:
            teacher += a[i] // c

answer = len(a) + teacher
print(answer)
