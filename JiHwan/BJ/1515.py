n = input()
answer = 0
while True:
    answer += 1
    num = str(answer)
    while len(num) > 0 and len(n) > 0:
        if num[0] == n[0]:
            n = n[1:]
        num = num[1:]
    if n == '':
        print(answer)
        break
