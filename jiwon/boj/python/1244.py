def switching(num):
    return 1 if num == 0 else 0


n = int(input())

s = list(map(int, input().split()))

for _ in range(int(input())):
    g, number = map(int, input().split())
    if g == 1:
        for i in range(number - 1, n, number):
            s[i] = switching(s[i])
    else:
        number -= 1
        left = number - 1
        right = number + 1
        s[number] = switching(s[number])
        while left >= 0 and right < n:
            if s[left] != s[right]:
                break
            s[left] = switching(s[left])
            s[right] = switching(s[right])
            left -= 1
            right += 1

a = list()
for i, item in enumerate(s, start=1):
    a.append(item)
    if i % 20 == 0:
        print(*a)
        a = list()
if a:
    print(*a)
