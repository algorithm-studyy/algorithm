# 입력 받기
a, amount_a = map(int, input().split())
b, amount_b = map(int, input().split())
c, amount_c = map(int, input().split())
count = 0

while count < 100:

    count += 1
    if count > 100:
        break

    if b < amount_a + amount_b:
        amount_a = amount_a + amount_b - b
        amount_b = b
    else:
        amount_b += amount_a
        amount_a = 0

    count += 1
    if count > 100:
        break

    if c < amount_b + amount_c:
        amount_b = amount_b + amount_c - c
        amount_c = c
    else:
        amount_c += amount_b
        amount_b = 0

    count += 1
    if count > 100:
        break

    if a < amount_a + amount_c:
        amount_c = amount_c + amount_a - a
        amount_a = a
    else:
        amount_a += amount_c
        amount_c = 0

print(amount_a)
print(amount_b)
print(amount_c)
print(count)