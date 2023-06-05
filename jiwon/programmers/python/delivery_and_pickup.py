# 택배가 제일 멀리 있으면 일단 거기까지는 가야함 ..
def get_not_zero_index(lst):
    for idx in range(len(lst) - 1, -1, -1):
        if lst[idx] != 0:
            return idx
    return 0


def delivery(d, i, cap):
    c = cap
    if i <= 0:
        return d, i
    while c > 0:
        c -= d[i]
        d[i] = -c if c < 0 else 0
        while i >= 0 and d[i] == 0:
            i -= 1
    return d, i


def pickup(p, j, cap):
    c = cap
    if j <= 0:
        return p, j
    while c < cap:
        c += p[j]
        p[j] = c - cap if c > cap else 0
        while j >= 0 and p[j] == 0:
            j -= 1
    return p, j


def solution(cap, n, d, p):
    answer = 0
    i, j = get_not_zero_index(d), get_not_zero_index(p)
    while i > 0 and j > 0:
        c = cap
        answer += max(i + 1, j + 1)
        d, i = delivery(d, i, cap)
        p, j = pickup(p, j, cap)
    return answer
