def solution(n, k):
    answer = 0
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    base = rev_base[::-1]
    base = base.split("0")

    for i in base:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue
        if int(i) == 2:
            answer += 1
            continue
        sosu = True
        for k in range(2, int(int(i) ** 0.5) + 1):  # 소수찾기
            if int(i) % k == 0:
                sosu = False
                break
        if sosu:
            answer += 1

    return answer