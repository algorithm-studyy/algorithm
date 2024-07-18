n, score, p = map(int, input().split())


def solution():
    if p == 0:
        return -1
    if n > 0:
        scores = list(map(int, input().split()))
    else:
        return 1
    rank = 1
    all_rank = 1
    for s in scores:
        if s > score:
            rank += 1
            all_rank += 1
        elif s == score:
            all_rank += 1
        else:
            return rank
        if all_rank > p:
            return -1
    return rank


print(solution())

